from pydantic import Field
from src.model.responder import ResponderOutput


class FormatterOutput(ResponderOutput):
    "The revision of your original output"

    references: list[str] = Field(description="citations that motivate your revision")
