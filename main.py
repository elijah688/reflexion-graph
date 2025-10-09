from langchain_core.messages import HumanMessage, ToolMessage, AIMessage
from langchain_openai import ChatOpenAI
from typing import Any
from src.chains.reviewer import make_reviewer_chain
from src.chains.formatter import make_formatter_chain
from src.chains.responder import make_responder_chain
from src.graph.graph import Graph
from src.graph.save import save_graph
from src.state.state import State

def get_last_message(res: dict[str, Any]) -> str | None:
    msgs: list[AIMessage | HumanMessage | ToolMessage] = res.get("messages", [])
    if len(msgs) > 0:
        return msgs[-1].text()
    return None


def main():
    llm = ChatOpenAI(model="gpt-4.1-mini")
    responder_agent = make_responder_chain(llm)
    reviewer_agent = make_reviewer_chain(llm)
    formatter_agent = make_formatter_chain(llm)

    graph = Graph(responder_agent, reviewer_agent, formatter_agent)
    app = graph.compile()

    bbytes: bytes = app.get_graph().draw_mermaid_png()
    save_graph(bbytes)
    res = app.invoke(
        input=State(
            max_iterations=3,
            iteration_count=1,
            messages=[
                HumanMessage(
                    "how to be a bodybuilder"
                )
            ],
        )
    )

    m = get_last_message(res)
    if m:
        print(m)


if __name__ == "__main__":
    main()
