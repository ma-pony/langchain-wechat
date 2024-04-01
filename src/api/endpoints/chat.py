from fastapi import APIRouter

from src.ai import chat_with_text

router = APIRouter()


@router.get("/chat_with_text", summary="文本聊天")
async def chat_with_text_api(
    text: str,
    session: str = "unused",
) -> str:
    """
    文本聊天
    :return:
    """
    return await chat_with_text(text, session)
