from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class QuerySearch(BaseModel):
    query: str = Field(..., min_length=1, max_length=200)

class SearchResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int
    rubrics: list[str]
    text: str
    created_date: datetime