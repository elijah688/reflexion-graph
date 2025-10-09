from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import Tool

serper = GoogleSerperAPIWrapper()
search = Tool(name="search", description="useful when u wanna search", func=serper.run)

tools = [search]
