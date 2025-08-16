from fastapi import APIRouter, Depends
from ..schemas import ChatRequest, ChatResponse, OrderStructured
from ..graph import chat_graph
from ..config import settings

router = APIRouter(prefix="/api/chat", tags=["chat"])

@router.post("/send", response_model=ChatResponse)
async def send(req: ChatRequest):
    state = {"last_user": req.message}
    result = chat_graph.invoke(state)
    return ChatResponse(reply=result["reply"], structured=OrderStructured(**result["structured"]))