from loguru import logger

from src.ai import chat_with_text
from src.dependencies import itchat
from src.models.wechat import MessageTypeEnum, GroupMessageModel


def is_call_me(message: GroupMessageModel):
    """
    判断是否是@我
    :return:
    """
    return message.is_at


# @itchat.msg_register(INCOME_MSG, isGroupChat=True)
def handle_group(msg):
    """
    监听群聊消息
    :param msg:
    :return:
    """
    logger.info(f"Message: {msg}")
    message = GroupMessageModel(**msg)
    logger.info(f"Message content: {message.content}")

    if not is_call_me(message):
        return
    if message.type == MessageTypeEnum.TEXT:
        res = chat_with_text(message.content)
        logger.info(res)
        logger.info(f"Text message: {message.content}")
        itchat.send(res, toUserName=message.from_user_id)