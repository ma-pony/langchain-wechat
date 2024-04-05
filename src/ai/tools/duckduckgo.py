from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_core.tools import Tool

wrapper = DuckDuckGoSearchAPIWrapper(region="cn-zh", max_results=10)
search = DuckDuckGoSearchResults(api_wrapper=wrapper)

duck_search_tool = Tool(
    name="Search",
    func=search.run,
    description="当您需要回答有关时事的问题时很有用",
)
