
from src.state.state import State

def has_tools(state: State):
    last_message = state.messages[-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return "formatter"
