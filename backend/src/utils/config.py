"""
Configuration module 

Loads and validates the config.yaml file using Pydantic models
Provides typed access to all technical parameters used across the project

Functions:
    load_config() -> AppConfig : Load and validate config.yaml.
"""

from pathlib import Path
from pydantic import BaseModel
from typing import List, Optional
import yaml


# Pydantic Models 

class EmbeddingConfig(BaseModel):
    model: str
    dim: int
    document_prefix: str = ""
    query_prefix: str = ""
    use_fp16: bool = False


class RAGConfig(BaseModel):
    chunk_size: int
    chunk_overlap: int
    csv_chunk_size: int
    top_k: int
    relevance_threshold: float
    min_chunk_score: Optional[float] = None

class RerankerConfig(BaseModel):
    model: str
    top_k: int

class RouterConfig(BaseModel):
    threshold: float


class LLMConfig(BaseModel):
    model: str
    multi_query_model: str
    ragas_judge_model: str = "llama3.1:8b"

class MultiQueryConfig(BaseModel):
    n_queries: int

class EmbeddingModelConfig(BaseModel):
    name: str
    dim: int
    document_prefix: str = ""
    query_prefix: str = ""
    batch_size: int = 8
    use_fp16: bool = False

class BenchmarkConfig(BaseModel):
    cloud_docs_path: str
    csv_path: str
    queries_path: str
    ground_truth_path: str
    n_runs: int
    top_k: int
    chunk_size: int = 500
    embedding_models: List[EmbeddingModelConfig]

class PathsConfig(BaseModel):
    data_raw: str
    results: str
    storage: str

class ApiConfig(BaseModel):
    collection_name: str


class AppConfig(BaseModel):
    embedding: EmbeddingConfig
    rag: RAGConfig
    llm: LLMConfig
    benchmark: BenchmarkConfig
    paths: PathsConfig
    reranker: RerankerConfig
    multi_query: MultiQueryConfig
    api: ApiConfig
    router: RouterConfig


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