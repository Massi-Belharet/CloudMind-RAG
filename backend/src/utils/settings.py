"""
Settings module 

Loads and validates environment variables


Functions:
    N/A — module-level settings instance only.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


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

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()