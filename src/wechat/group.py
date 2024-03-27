from loguru import logger

from src.ai import chat_with_text
from src.dependencies import itchat
from src.models.wechat import GroupMessageModel, MessageTypeEnum
from src.wechat.base import filter_message


def is_call_me(message: GroupMessageModel):
    """
    判断是否是@我
    :return:
    """
    return message.is_at


@filter_message(model=GroupMessageModel)
def handle_group(message: GroupMessageModel):
    """
    监听群聊消息
    :param message:
    :return:
    """
    logger.info(f"Message content: {message.content}")

    if not is_call_me(message):
        return
    if message.type == MessageTypeEnum.TEXT:
        res = chat_with_text(message.content, session_id=f"{message.from_user_id}-{message.to_user_id}")
        logger.info(res)
        logger.info(f"Text message: {message.content}")
        itchat.send(res, toUserName=message.from_user_id)
