from src.state.state import State
from langgraph.graph import END


def should_end(state: State) -> str:
    if state.iteration_count > state.max_iterations:
        return END

    return "reviewer"
