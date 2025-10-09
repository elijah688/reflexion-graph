from langchain_openai import ChatOpenAI
from langchain_core.runnables.base import RunnableSerializable
from src.model.responder import ResponderOutput
from src.prompt_templates.responder import responder_template


def make_responder_chain(llm: ChatOpenAI) -> RunnableSerializable:
    return responder_template | llm.with_structured_output(ResponderOutput)
