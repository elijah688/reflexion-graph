from langchain_openai import ChatOpenAI
from langchain_core.runnables.base import RunnableSerializable
from src.model.formatter import FormatterOutput
from src.prompt_templates.formatter import formatter_template


def make_formatter_chain(llm: ChatOpenAI) -> RunnableSerializable:
    return formatter_template | llm.with_structured_output(FormatterOutput)
