from loguru import logger

from src.ai import chat_with_text
from src.dependencies import itchat
from src.models.wechat import MessageModel, MessageTypeEnum


# @itchat.msg_register(INCOME_MSG)
def handle_single(msg):
    """
    监听私聊消息
    :param msg:
    :return:
    """
    logger.info(f"Message: {msg}")
    message = MessageModel(**msg)
    logger.info(f"Message content: {message.content}")
    if message.type == MessageTypeEnum.TEXT:
        res = chat_with_text(message.content)
        logger.info(res)
        logger.info(f"Text message: {message.content}")
        itchat.send(res, toUserName=message.from_user_id)
