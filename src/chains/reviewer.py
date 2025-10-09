from langchain_openai import ChatOpenAI
from langchain_core.runnables.base import RunnableSerializable
from src.prompt_templates.reviewer import reviewer_agent_template
from src.tools.tools import tools


def make_reviewer_chain(llm: ChatOpenAI) -> RunnableSerializable:
    return reviewer_agent_template | llm.bind_tools(tools)
