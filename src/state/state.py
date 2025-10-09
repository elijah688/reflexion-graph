from pydantic import BaseModel
from langgraph.graph import add_messages
from typing import Annotated


class State(BaseModel):
    messages: Annotated[list, add_messages]
    iteration_count: int
    max_iterations: int
