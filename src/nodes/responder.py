from src.state.state import State
from src.model.responder import ResponderOutput
from langchain_core.messages import AIMessage
from langchain_core.runnables.base import RunnableSerializable


class ResponderNode:
    def __init__(self, responder_agent: RunnableSerializable):
        self.responder_agent = responder_agent

    def node_fn(self):
        def node(state: State):
            res: ResponderOutput = self.responder_agent.invoke(
                input={"messages": state.messages[-1:]}
            )

            return {
                "iteration_count": state.iteration_count,
                "messages": [AIMessage(res.model_dump_json())],
            }

        return node
