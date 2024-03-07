from enum import Enum

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
    member_list: list = Field(default=None, alias="MemberList")
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
    msg_id: str = Field(..., alias="MsgId")
    from_user_id: str = Field(..., alias="FromUserName")
    to_user_id: str = Field(..., alias="ToUserName")
    msg_type: int = Field(..., alias="MsgType")
    content: str = Field(..., alias="Content")
    status: int = Field(..., alias="Status")
    img_status: int = Field(..., alias="ImgStatus")
    create_time: int = Field(..., alias="CreateTime")
    voice_length: int = Field(..., alias="VoiceLength")
    play_length: int = Field(..., alias="PlayLength")
    file_name: str = Field(..., alias="FileName")
    file_size: str = Field(..., alias="FileSize")
    media_id: str = Field(..., alias="MediaId")
    url: str = Field(..., alias="Url")
    app_msg_type: int = Field(..., alias="AppMsgType")
    status_notify_code: int = Field(..., alias="StatusNotifyCode")
    status_notify_user_name: str = Field(..., alias="StatusNotifyUserName")
    recommend_info: RecommendInfoModel = Field(..., alias="RecommendInfo")
    forward_flag: int = Field(..., alias="ForwardFlag")
    app_info: dict = Field(..., alias="AppInfo")
    has_product_id: int = Field(..., alias="HasProductId")
    ticket: str = Field(..., alias="Ticket")
    img_height: int = Field(..., alias="ImgHeight")
    img_width: int = Field(..., alias="ImgWidth")
    sub_msg_type: int = Field(..., alias="SubMsgType")
    new_msg_id: int = Field(..., alias="NewMsgId")
    ori_content: str = Field(..., alias="OriContent")
    encry_file_name: str = Field(..., alias="EncryFileName")
    user: UserModel = Field(..., alias="User")
    type: MessageTypeEnum = Field(..., alias="Type")
    text: str | list[str] = Field(..., alias="Text")
    system_info: str = Field(default=None, alias="SystemInfo")
