from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

wrapper = DuckDuckGoSearchAPIWrapper(region="cn-zh", max_results=10)
search = DuckDuckGoSearchResults(api_wrapper=wrapper)
