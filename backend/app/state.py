from typing import TypedDict, List
from langchain_core.messages import AnyMessage

class BotState(TypedDict):
    messages: List[AnyMessage]
    cart: list