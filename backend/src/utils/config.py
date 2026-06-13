"""
Configuration module 

Loads and validates the config.yaml file using Pydantic models
Provides typed access to all technical parameters used across the project

Functions:
    load_config() -> AppConfig : Load and validate config.yaml.
"""

from pathlib import Path
from pydantic import BaseModel
import yaml


# Pydantic Models 

class EmbeddingConfig(BaseModel):
    model: str
    dim: int
    document_prefix: str = ""
    query_prefix: str = ""


class RAGConfig(BaseModel):
    chunk_size: int
    chunk_overlap: int
    csv_chunk_size: int
    top_k: int

class RerankerConfig(BaseModel):
    model: str
    top_k: int


class LLMConfig(BaseModel):
    model: str

class MultiQueryConfig(BaseModel):
    n_queries: int


class BenchmarkConfig(BaseModel):
    cloud_docs_path: str
    csv_path: str
    queries_path: str
    n_runs: int
    top_k: int


class PathsConfig(BaseModel):
    data_raw: str
    results: str
    storage: str


class AppConfig(BaseModel):
    embedding: EmbeddingConfig
    rag: RAGConfig
    llm: LLMConfig
    benchmark: BenchmarkConfig
    paths: PathsConfig
    reranker: RerankerConfig
    multi_query: MultiQueryConfig


# Loader 

def load_config(config_path: str = "backend/config/config.yaml") -> AppConfig:
    """
    Load and validate the config.yaml file.

    Args:
        config_path (str): Path to the config.yaml file.

    Returns:
        AppConfig: Validated configuration object.

    Raises:
        FileNotFoundError: If the config file does not exist.
    """
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(path, "r") as f:
        data = yaml.safe_load(f)

    return AppConfig(**data)


config = load_config()