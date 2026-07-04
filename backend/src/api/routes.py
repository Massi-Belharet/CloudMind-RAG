"""
API routes

Exposes the production RAG pipeline over HTTP: a health check endpoint and
the main question-answering endpoints (blocking and streaming).

Functions:
    health() -> HealthResponse : Report that the API is running.
    ask(request: AskRequest) -> AskResponse : Answer a user question using the RAG pipeline.
    ask_stream(request: AskRequest) -> StreamingResponse : Stream an answer as Server-Sent Events.
    _sse_stream(pipeline: Pipeline, query: str, k: int) -> Iterator[str] : Format pipeline.ask_stream() fragments as SSE events.
"""

import json
from typing import Iterator

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse

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


def _sse_stream(pipeline: Pipeline, query: str, k: int) -> Iterator[str]:
    """
    Format pipeline.ask_stream() text fragments as Server-Sent Events.

    Each event's data field is a JSON object — {"chunk": "..."} for a text
    fragment, or {"error": "..."} if the pipeline raises mid-stream (the
    response has already started by then, so an HTTP error status can no
    longer be sent — the error is surfaced as an SSE event instead).

    Args:
        pipeline (Pipeline): The cached production RAG pipeline.
        query (str): The user's query.
        k (int): Number of chunks to retrieve.

    Yields:
        str: SSE-formatted event strings.
    """
    try:
        for chunk in pipeline.ask_stream(query, k):
            yield f"data: {json.dumps({'chunk': chunk})}\n\n"
    except Exception as exc:
        yield f"data: {json.dumps({'error': str(exc)})}\n\n"


@router.post("/ask/stream")
def ask_stream(request: AskRequest, pipeline: Pipeline = Depends(get_pipeline)) -> StreamingResponse:
    """
    Answer a user question using the production RAG pipeline, streaming the
    response as Server-Sent Events instead of waiting for the full answer.

    Args:
        request (AskRequest): The user's query and desired number of chunks.
        pipeline (Pipeline): The cached production RAG pipeline, injected by FastAPI.

    Returns:
        StreamingResponse: A text/event-stream response of {"chunk": "..."}
        events, or a single {"error": "..."} event if generation fails.
    """
    return StreamingResponse(
        _sse_stream(pipeline, request.query, request.k),
        media_type="text/event-stream",
    )