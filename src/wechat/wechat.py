import os
from enum import Enum

import qrcode
from loguru import logger

from config import settings
from src.dependencies import itchat
from src.dependencies.itchat.content import INCOME_MSG
from src.wechat.group import handle_group
from src.wechat.single import handle_single


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


def start_channel():
    # register message listener
    itchat.msg_register(INCOME_MSG)(handle_single)
    itchat.msg_register(INCOME_MSG, isGroupChat=True)(handle_group)

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
