from pydantic import BaseModel, Field

class Reflection(BaseModel):
    missing: str = Field(
        description="things to include cuz they're useful and would have impact"
    )
    unnecessary: str = Field(description="thisng to cut out cuz they aint relevant")


class ResponderOutput(BaseModel):
    report: str = Field(description="the report you need to generate")
    reflection: Reflection = Field(
        description="the harsh critique of your work for how it can be dramatically improved"
    )
    search_terms: list[str] = Field(
        description="the list of search tearms that would yieald information that will make your report so much better"
    )
