from langchain_core.runnables.base import RunnableSerializable
from src.state.state import State
from langchain_core.messages import HumanMessage


class ReviewerNode:
    def __init__(self, reviewer_agent: RunnableSerializable):
        self.reviewer_agent = reviewer_agent

    def node_fn(self):
        def node(state: State):
            content: str = state.messages[-1].text()

            res = self.reviewer_agent.invoke(
                input={"messages": [*state.messages, HumanMessage(content)]}
            )
            return {
                "messages": [res],
            }

        return node
