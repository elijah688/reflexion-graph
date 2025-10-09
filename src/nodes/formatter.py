from src.state.state import State
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.runnables.base import RunnableSerializable
from typing import Union
from src.model.formatter import FormatterOutput
from langchain_core.messages import RemoveMessage

Message = Union[AIMessage, HumanMessage, ToolMessage]


class FormatterNode:
    def __init__(self, formatter_agent: RunnableSerializable):
        self.formatter_agent = formatter_agent

    def __from_last_ai_message_content(self, state: State):
        messages: list[Message] = state.messages

        last_ai_message_index = -1
        for i, m in enumerate(messages):
            if isinstance(m, AIMessage):
                last_ai_message_index = i - 1
        if last_ai_message_index < 0:
            raise ValueError("can't have negative index: no ai messages found")

        x: Message = state.messages[last_ai_message_index]
        return x.text()

    def node_fn(self):
        def node(state: State):
            print("iterration", state.iteration_count)
            content = self.__from_last_ai_message_content(state)
            res: FormatterOutput = self.formatter_agent.invoke(
                input={"messages": [HumanMessage(content)]}
            )
            return {
                "iteration_count": state.iteration_count + 1,
                "messages": [
                    *[RemoveMessage(m.id) for m in state.messages],
                    HumanMessage(res.model_dump_json()),
                ],
            }

        return node
