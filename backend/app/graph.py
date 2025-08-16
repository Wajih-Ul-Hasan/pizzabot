from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from .schemas import OrderStructured, Item
from .llm import get_chat_model
from .vectorstore import get_vectordb
from .config import settings
from .menu import MENU

parser = PydanticOutputParser(pydantic_object=OrderStructured)

SYSTEM = """
You are PizzaBot, an ordering assistant for a pizza shop. Keep replies short. When user asks menu or ingredients, answer first then attach 1-3 suggestions. Always produce JSON matching the given schema.
Pricing is decided by MENU. If quantity missing assume 1. If size missing ask a follow-up and set intent=order.create with empty items.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM + "\nResponse JSON schema: {format_instructions}"),
    ("human", "Context: {context}\nUser: {user_input}")
]).partial(format_instructions=parser.get_format_instructions())


def build_graph():
    sg = StateGraph(state_schema=dict)

    def llm_node(state):
        llm = get_chat_model()
        # Build context from vector DB and menu
        docs = get_vectordb(settings.vectordb_dir).search(state.get("last_user", ""))
        snippets = "\n".join([d.page_content for d in docs])
        menu_lines = [f"{m['name']} ({'/'.join([f'{k}:{v}' for k,v in m['price_by_size'].items()])})" for m in MENU]
        ctx = f"Menu: {'; '.join(menu_lines)}\nDocs: {snippets}"
        structured = llm.with_structured_output(OrderStructured)
        out: OrderStructured = structured.invoke(prompt.format(context=ctx, user_input=state["last_user"]))
        reply = build_reply(out)
        return {"reply": reply, "structured": out.model_dump()}

    def build_reply(out: OrderStructured) -> str:
        if out.intent == "info.menu":
            return "Here is the menu: " + ", ".join([m["name"] for m in MENU])
        if out.intent.startswith("order") and out.items:
            total = sum(i.price * i.quantity for i in out.items)
            names = ", ".join([f"{i.quantity}x {i.size} {i.name}" for i in out.items])
            return f"Added {names}. Total so far ${total:.2f}. Anything else?"
        if out.intent == "smalltalk":
            return "Hello. Would you like to see specials?"
        return "Got it. What size and quantity?"

    sg.add_node("llm", llm_node)
    sg.set_entry_point("llm")
    sg.add_edge("llm", END)
    return sg.compile()

chat_graph = build_graph()