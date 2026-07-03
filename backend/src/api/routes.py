"""
API routes 

Exposes the production RAG pipeline over HTTP: a health check endpoint and
the main question-answering endpoint.

Functions:
    health() -> HealthResponse : Report that the API is running.
    ask(request: AskRequest) -> AskResponse : Answer a user question using the RAG pipeline.
"""

from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import get_pipeline
from src.api.schemas import AskRequest, AskResponse, HealthResponse
from src.rag.pipeline import Pipeline

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """
    Report that the API is running.

    Returns:
        HealthResponse: A simple status confirmation.
    """
    return HealthResponse(status="ok")


@router.post("/ask", response_model=AskResponse)
def ask(request: AskRequest, pipeline: Pipeline = Depends(get_pipeline)) -> AskResponse:
    """
    Answer a user question using the production RAG pipeline.

    Args:
        request (AskRequest): The user's query and desired number of chunks.
        pipeline (Pipeline): The cached production RAG pipeline, injected by FastAPI.

    Returns:
        AskResponse: The generated answer.

    Raises:
        HTTPException: If the pipeline fails to produce a response.
    """
    try:
        response = pipeline.ask(request.query, request.k)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return AskResponse(response=response)