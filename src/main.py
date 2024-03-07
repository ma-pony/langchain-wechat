import os
import sys
from enum import Enum

from fastapi import FastAPI
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from loguru import logger
from pyqrcode import QRCode

from config import settings
from src.dependencies import itchat
import qrcode

from src.dependencies.itchat.content import TEXT, VOICE, PICTURE, NOTE, ATTACHMENT, \
    SHARING, INCOME_MSG
from src.models.wechat import MessageModel, MessageTypeEnum


def main():
    chat = ChatOpenAI(
        openai_api_key=settings.OPENAI_API_KEY,
        model_name=settings.OPENAI_MODEL,
    )
    res = chat.invoke(
        [
            HumanMessage(
                content="Translate this sentence from English to French: I am programming."
            )
        ]
    )

    print(res)


class ContextType(Enum):
    TEXT = 1  # 文本消息
    VOICE = 2  # 音频消息
    IMAGE = 3  # 图片消息
    FILE = 4  # 文件信息
    VIDEO = 5  # 视频信息
    SHARING = 6  # 分享信息

    IMAGE_CREATE = 10  # 创建图片命令
    ACCEPT_FRIEND = 19  # 同意好友请求
    JOIN_GROUP = 20  # 加入群聊
    PATPAT = 21  # 拍了拍
    FUNCTION = 22  # 函数调用
    EXIT_GROUP = 23  # 退出


# 可用的二维码生成接口
# https://api.qrserver.com/v1/create-qr-code/?size=400×400&data=https://www.abc.com
# https://api.isoyu.com/qr/?m=1&e=L&p=20&url=https://www.abc.com
def qrcode_callback(uuid, status, qr_code):
    url = f"https://login.weixin.qq.com/l/{uuid}"

    if status == "0":
        logger.info("QR code scanned")
        qr = qrcode.QRCode(border=1)
        qr.add_data(url)
        qr.make(fit=True)
        qr.print_ascii(invert=True)
    elif status == "200":
        logger.info("QR code confirmed")
    elif status == "201":
        logger.info("QR code scanned, waiting for confirmation")
    else:
        logger.info(f"QR code status: {status}")


def login_callback(*args, **kwargs):
    user_id = itchat.instance.storageClass.userName
    name = itchat.instance.storageClass.nickName
    logger.info(f"Wechat login success, user_id: {user_id}, nickname: {name}")


def logout_callback(*args, **kwargs):
    user_id = itchat.instance.storageClass.userName
    name = itchat.instance.storageClass.nickName
    logger.info(f"Wechat logout Success, user_id: {user_id}, nickname: {name}")


@itchat.msg_register(INCOME_MSG)
def handle_single(cmsg):
    """"""
    logger.info(f"Message: {cmsg}")
    message = MessageModel(**cmsg)
    logger.info(f"Message content: {message.content}")
    if message.type == MessageTypeEnum.TEXT:
        logger.info(f"Text message: {message.content}")


def start_channel():
    itchat.instance.receivingRetryCount = 600  # 修改断线超时时间
    status_path = os.path.join("itchat.pkl")
    itchat.auto_login(
        enableCmdQR=2,
        hotReload=settings.WECHAT_HOT_RELOAD,
        statusStorageDir=status_path,
        qrCallback=qrcode_callback,
        exitCallback=logout_callback,
        loginCallback=login_callback
    )

    # start message listener
    itchat.run()


app = FastAPI(title=settings.PROJECT_NAME)

app.add_event_handler("startup", start_channel)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
