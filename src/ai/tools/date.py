from datetime import datetime

from langchain_core.tools import Tool, tool


@tool
def get_current_date(query: str) -> str:
    """获取当前日期"""
    return datetime.now().strftime("%Y-%m-%d")


@tool
def get_current_datetime(query: str) -> str:
    """获取当前时间"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


current_date_tool = Tool(
    name="CurrentDate",
    func=get_current_date,
    description="需要获取当前日期的时候很有用",
)
current_datetime_tool = Tool(
    name="CurrentDatetime",
    func=get_current_datetime,
    description="需要获取当前时间的时候很有用",
)
