from fastapi import APIRouter
from ..menu import MENU

router = APIRouter(prefix="/api/order", tags=["order"])

@router.get("/menu")
async def menu():
    return {"menu": MENU}