from fastapi import APIRouter

from src.api.endpoints import chat

api_router = APIRouter()
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])


@api_router.get("/health_check")
async def health_check():
    """
    健康检查
    :return:
    """
    return {"status": "ok"}
