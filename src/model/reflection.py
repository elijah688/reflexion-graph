from pydantic import BaseModel, Field

class Reflection(BaseModel):
    "Your reflection on the report you produced"
    missing: str = Field(
        description="things to include cuz they're useful and would have impact"
    )
    unnecessary: str = Field(description="thisng to cut out cuz they aint relevant")
