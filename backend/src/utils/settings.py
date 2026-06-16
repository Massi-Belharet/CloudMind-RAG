"""
Settings module 

Loads and validates environment variables


Functions:
    N/A — module-level settings instance only.
"""

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):

    # Qdrant
    qdrant_host: str
    qdrant_port: int

    # Pgvector
    postgres_host: str
    postgres_port: int
    postgres_db: str
    postgres_user: str
    postgres_password: str

    # LLM
    ollama_host: str
    ollama_port: int

    # LangSmith
    langsmith_tracing: bool
    langsmith_api_key: str
    langsmith_project: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()