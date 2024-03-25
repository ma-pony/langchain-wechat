from datetime import datetime

from langchain_core.tools import tool


@tool
def get_current_date(query: str) -> str:
    """获取当前日期"""
    return datetime.now().strftime("%Y-%m-%d")


@tool
def get_current_datetime(query: str) -> str:
    """获取当前时间"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
