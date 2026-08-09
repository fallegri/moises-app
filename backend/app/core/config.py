"""Application settings using pydantic-settings."""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    # AI Provider Configuration
    ai_api_key: str = ""
    ai_base_url: str = "https://integrate.api.nvidia.com/v1"
    ai_model: str = "meta/llama-3.1-405b-instruct"

    # Knowledge Base
    knowledge_base_path: str = "../skills/knowledge"

    # Storage
    storage_path: str = "./storage"

    # Application
    app_name: str = "Research Assistant API"
    debug: bool = False
    cors_origins: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
