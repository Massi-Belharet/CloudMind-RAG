"""
Pydantic request and response schemas 
"""

from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    query: str = Field(..., min_length=1, description="User question to answer.")
    k: int = Field(default=5, gt=0, description="Number of chunks to retrieve.")


class AskResponse(BaseModel):
    response: str


class HealthResponse(BaseModel):
    status: str