import time
from functools import partial, wraps

from loguru import logger
from redis import Redis

from config import settings
from src.models.wechat import MessageModel

redis_client = Redis.from_url(settings.REDIS_URL)
message_filter_key = "message_filter:wechat_message"
message_capacity = 1_000_000


# 过滤过期消息
def filter_expired(message: MessageModel, expire_seconds=60):
    """
    过滤过期消息
    :param message:
    :param expire_seconds:
    :return:
    """
    return int(message.create_time) < int(time.time() - expire_seconds)


# 过滤重复消息
def filter_repeat(message: MessageModel):
    """
    过滤重复消息
    :param message:
    :return:
    """
    cuckoo_filter = redis_client.cf()
    if not redis_client.exists(message_filter_key):
        cuckoo_filter.create(message_filter_key, message_capacity)
    if cuckoo_filter.exists(message_filter_key, message.msg_id):
        return True
    cuckoo_filter.addnx(message_filter_key, message.msg_id)
    return False


def filter_message(func=None, *, model=None, expire=True, repeat=True, expire_seconds=60):
    """
    过滤消息
    :param model:
    :param func:
    :param expire:
    :param repeat:
    :param expire_seconds:
    :return:
    """
    if func is None:
        return partial(filter_message, model=model, expire=expire, repeat=repeat, expire_seconds=expire_seconds)

    @wraps(func)
    def wrapper(msg):
        logger.info(f"Receive message: {msg}")
        message = model(**msg) if model else msg
        if expire and filter_expired(message, expire_seconds):
            return
        if repeat and filter_repeat(message):
            return
        return func(message)

    return wrapper
