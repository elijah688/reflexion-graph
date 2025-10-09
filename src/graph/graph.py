from src.tools.tools import tools

from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, END
from langgraph.graph.state import CompiledStateGraph
from src.nodes import ResponderNode, FormatterNode, ReviewerNode, should_end
from langchain_core.runnables.base import RunnableSerializable
from src.nodes.has_tools import has_tools

from src.state.state import State


class Graph:
    def __init__(
        self,
        responder_agent: RunnableSerializable,
        reviewer_node: RunnableSerializable,
        formatter_node: RunnableSerializable,
    ):
        self.graph = StateGraph(State)
        self.responder_node = ResponderNode(responder_agent)
        self.reviewer_node = ReviewerNode(reviewer_node)
        self.formatter_node = FormatterNode(formatter_node)

        # NODES
        self.graph.add_node("responder", self.responder_node.node_fn())
        self.graph.add_node("tools", ToolNode(tools=tools))
        self.graph.add_node("reviewer", self.reviewer_node.node_fn())
        self.graph.add_node("formatter", self.formatter_node.node_fn())

        # EDGES
        self.graph.add_edge("responder", "reviewer")
        self.graph.add_conditional_edges(
            "reviewer", has_tools, {"tools": "tools", "formatter": "formatter"}
        )
        self.graph.add_edge("tools", "reviewer")
        self.graph.add_conditional_edges(
            "formatter", should_end, {"reviewer": "reviewer", END: END}
        )

        self.graph.set_entry_point("responder")

    def compile(self) -> CompiledStateGraph[State, None, State, State]:
        return self.graph.compile()
