from pydantic import BaseModel, Field, conlist
from typing import List, Optional, Literal, Annotated

class ChatMessage(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str

class ChatRequest(BaseModel):
    session_id: str
    message: str
    history: List[ChatMessage] = Field(default_factory=list)

class Suggestion(BaseModel):
    text: str

class Item(BaseModel):
    sku: str
    name: str
    size: Literal["small", "medium", "large"]
    quantity: int
    price: float

class OrderStructured(BaseModel):
    intent: Literal["order.create", "order.modify", "info.menu", "smalltalk", "unknown"]
    items: List[Item] = Field(default_factory=list)
    notes: Optional[str] = None
    suggestions: Annotated[list[Suggestion], Field(max_length=3)] = Field(default_factory=list)

class ChatResponse(BaseModel):
    reply: str
    structured: OrderStructured

class MenuItem(BaseModel):
    sku: str
    name: str
    description: str
    sizes: List[str]
    price_by_size: dict

class IngestDoc(BaseModel):
    id: str
    text: str