from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import chat, order, ingest
from .config import settings

app = FastAPI(title=settings.app_name)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)
app.include_router(order.router)
app.include_router(ingest.router)

@app.get("/health")
async def health():
    return {"status": "ok"}