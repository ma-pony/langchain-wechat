from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field


class RecommendInfoModel(BaseModel):
    user_name: str = Field(..., alias="UserName")
    nick_name: str = Field(..., alias="NickName")
    qq_num: int = Field(..., alias="QQNum")
    province: str = Field(..., alias="Province")
    city: str = Field(..., alias="City")
    content: str = Field(..., alias="Content")
    signature: str = Field(..., alias="Signature")
    alias: str = Field(..., alias="Alias")
    scene: int = Field(..., alias="Scene")
    verify_flag: int = Field(..., alias="VerifyFlag")
    attr_status: int = Field(..., alias="AttrStatus")
    sex: int = Field(..., alias="Sex")
    ticket: str = Field(..., alias="Ticket")
    op_code: int = Field(..., alias="OpCode")


class UserModel(BaseModel):
    member_list: list[Any] = Field(default=None, alias="MemberList")
    uin: int = Field(..., alias="Uin")
    user_name: str = Field(..., alias="UserName")
    nick_name: str = Field(..., alias="NickName")
    head_img_url: str = Field(..., alias="HeadImgUrl")
    contact_flag: int = Field(..., alias="ContactFlag")
    member_count: int = Field(..., alias="MemberCount")
    remark_name: str = Field(..., alias="RemarkName")
    hide_input_bar_flag: int = Field(..., alias="HideInputBarFlag")
    sex: int = Field(..., alias="Sex")
    signature: str = Field(..., alias="Signature")
    verify_flag: int = Field(..., alias="VerifyFlag")
    owner_uin: int = Field(..., alias="OwnerUin")
    py_initial: str = Field(..., alias="PYInitial")
    py_quan_pin: str = Field(..., alias="PYQuanPin")
    remark_py_initial: str = Field(..., alias="RemarkPYInitial")
    remark_py_quan_pin: str = Field(..., alias="RemarkPYQuanPin")
    star_friend: int = Field(..., alias="StarFriend")
    app_account_flag: int = Field(..., alias="AppAccountFlag")
    statues: int = Field(..., alias="Statues")
    attr_status: int = Field(..., alias="AttrStatus")
    province: str = Field(..., alias="Province")
    city: str = Field(..., alias="City")
    alias: str = Field(..., alias="Alias")
    sns_flag: int = Field(..., alias="SnsFlag")
    uni_friend: int = Field(..., alias="UniFriend")
    display_name: str = Field(..., alias="DisplayName")
    chat_room_id: int = Field(..., alias="ChatRoomId")
    key_word: str = Field(..., alias="KeyWord")
    encry_chat_room_id: str = Field(..., alias="EncryChatRoomId")
    is_owner: int = Field(default=None, alias="IsOwner")
    web_wx_plugin_switch: int = Field(default=None, alias="WebWxPluginSwitch")
    head_img_flag: int = Field(default=None, alias="HeadImgFlag")


class MessageTypeEnum(str, Enum):
    TEXT = "Text"
    PICTURE = "Picture"
    MAP = "Map"
    CARD = "Card"
    SHARING = "Sharing"
    RECORDING = "Recording"
    ATTACHMENT = "Attachment"
    VIDEO = "Video"
    FRIENDS = "Friends"
    SYSTEM = "System"


class MessageModel(BaseModel):
    msg_id: str = Field(default=None, alias="MsgId")
    from_user_id: str = Field(..., alias="FromUserName")
    to_user_id: str = Field(..., alias="ToUserName")
    msg_type: int = Field(default=None, alias="MsgType")
    content: str = Field(default=None, alias="Content")
    status: int = Field(default=None, alias="Status")
    img_status: int = Field(default=None, alias="ImgStatus")
    create_time: int = Field(default=None, alias="CreateTime")
    voice_length: int = Field(default=None, alias="VoiceLength")
    play_length: int = Field(default=None, alias="PlayLength")
    file_name: str = Field(default=None, alias="FileName")
    file_size: str = Field(default=None, alias="FileSize")
    media_id: str = Field(default=None, alias="MediaId")
    url: str = Field(default=None, alias="Url")
    app_msg_type: int = Field(default=None, alias="AppMsgType")
    status_notify_code: int = Field(default=None, alias="StatusNotifyCode")
    status_notify_user_name: str = Field(default=None, alias="StatusNotifyUserName")
    recommend_info: RecommendInfoModel = Field(default=None, alias="RecommendInfo")
    forward_flag: int = Field(default=None, alias="ForwardFlag")
    app_info: dict[str, Any] = Field(default=None, alias="AppInfo")
    has_product_id: int = Field(default=None, alias="HasProductId")
    ticket: str = Field(default=None, alias="Ticket")
    img_height: int = Field(default=None, alias="ImgHeight")
    img_width: int = Field(default=None, alias="ImgWidth")
    sub_msg_type: int = Field(default=None, alias="SubMsgType")
    new_msg_id: int = Field(default=None, alias="NewMsgId")
    ori_content: str = Field(default=None, alias="OriContent")
    encry_file_name: str = Field(default=None, alias="EncryFileName")
    user: UserModel = Field(..., alias="User")
    type: MessageTypeEnum = Field(..., alias="Type")
    text: str | list[str] = Field(..., alias="Text")
    system_info: str = Field(default=None, alias="SystemInfo")


class ChatRoomMember(BaseModel):
    member_list: list[Any] = Field(default=None, alias="MemberList")
    uin: int = Field(..., alias="Uin")
    user_name: str = Field(..., alias="UserName")
    nick_name: str = Field(..., alias="NickName")
    attr_status: int = Field(..., alias="AttrStatus")
    py_initial: str = Field(..., alias="PYInitial")
    remark_py_initial: str = Field(..., alias="RemarkPYInitial")
    remark_py_quan_pin: str = Field(..., alias="RemarkPYQuanPin")
    member_status: int = Field(..., alias="MemberStatus")
    display_name: str = Field(..., alias="DisplayName")
    key_word: str = Field(..., alias="KeyWord")


class GroupModel(UserModel):
    is_admin: Optional[int] = Field(default=None, alias="IsAdmin")
    self: ChatRoomMember = Field(..., alias="Self")
    head_img_update_flag: int = Field(default=None, alias="HeadImgUpdateFlag")
    contact_type: int = Field(default=None, alias="ContactType")
    chat_room_owner: str = Field(default=None, alias="ChatRoomOwner")


class GroupMessageModel(MessageModel):
    group: GroupModel = Field(..., alias="User")
    actual_nick_name: str = Field(..., alias="ActualNickName")
    is_at: bool = Field(..., alias="IsAt")
    actual_user_name: str = Field(..., alias="ActualUserName")
