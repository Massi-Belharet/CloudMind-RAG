"""
FastAPI application entry point 

Preloads the production RAG pipeline at startup so the first request isn't
penalized by model loading (bge-m3, bge-reranker-v2-m3), then serves the
/health and /ask endpoints.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.dependencies import get_pipeline
from src.api.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Preloading production RAG pipeline...")
    get_pipeline()
    print("Pipeline ready")
    yield


app = FastAPI(title="CloudMind RAG API", lifespan=lifespan)
app.include_router(router)