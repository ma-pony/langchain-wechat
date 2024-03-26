from loguru import logger

from src.ai import chat_with_text
from src.dependencies import itchat
from src.models.wechat import MessageModel, MessageTypeEnum
from src.wechat.base import filter_message


# @itchat.msg_register(INCOME_MSG)
@filter_message
def handle_single(message: MessageModel):
    """
    监听私聊消息
    :param message:
    :return:
    """
    logger.info(f"Message content: {message.content}")
    if message.type == MessageTypeEnum.TEXT:
        res = chat_with_text(message.content, session_id=f"{message.from_user_id}-{message.to_user_id}")
        logger.info(res)
        logger.info(f"Text message: {message.content}")
        itchat.send(res, toUserName=message.from_user_id)
