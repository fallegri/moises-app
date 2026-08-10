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

    # Database (PostgreSQL via NeonTech/Railway)
    database_url: Optional[str] = None

    # Frontend URL for CORS (Vercel deployment)
    frontend_url: Optional[str] = None

    # Application
    app_name: str = "Research Assistant API"
    debug: bool = False
    cors_origins: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    @property
    def effective_cors_origins(self) -> list[str]:
        """Return CORS origins including FRONTEND_URL if set."""
        origins = list(self.cors_origins)
        if self.frontend_url and self.frontend_url not in origins:
            origins.append(self.frontend_url)
        return origins

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
