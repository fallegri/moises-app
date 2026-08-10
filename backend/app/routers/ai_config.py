"""AI configuration endpoints for runtime API key, base URL, and model management."""

import json
from pathlib import Path
from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

from app.core.config import settings
from app.services.persistence import get_persistence_service

router = APIRouter()

# Persistence service for AI config storage
_persistence = get_persistence_service()

# Path to the persisted AI configuration file (used by JSON fallback and tests)
_CONFIG_FILE = Path(settings.storage_path) / "ai_config.json"


class AIConfigRequest(BaseModel):
    """Request model for updating AI configuration."""
    api_key: str = ""
    base_url: str = ""
    model: str = ""


class AIConfigResponse(BaseModel):
    """Response model with masked API key."""
    api_key_masked: str
    base_url: str
    model: str
    is_configured: bool


def _mask_api_key(key: str) -> str:
    """Mask the API key showing only the last 4 characters."""
    if not key or len(key) <= 4:
        return "****" if key else ""
    return "*" * (len(key) - 4) + key[-4:]


def load_ai_config() -> Optional[dict]:
    """Load AI configuration from persistent storage."""
    if not _CONFIG_FILE.exists():
        return None
    try:
        data = json.loads(_CONFIG_FILE.read_text(encoding="utf-8"))
        return data
    except (json.JSONDecodeError, OSError):
        return None


def save_ai_config(config: dict) -> None:
    """Save AI configuration to persistent storage."""
    _CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    _CONFIG_FILE.write_text(
        json.dumps(config, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


@router.get("", response_model=AIConfigResponse)
async def get_ai_config():
    """Get the current AI configuration with masked API key."""
    config = load_ai_config()

    if config and config.get("api_key"):
        return AIConfigResponse(
            api_key_masked=_mask_api_key(config["api_key"]),
            base_url=config.get("base_url", settings.ai_base_url),
            model=config.get("model", settings.ai_model),
            is_configured=True,
        )

    # Fall back to .env settings
    return AIConfigResponse(
        api_key_masked=_mask_api_key(settings.ai_api_key),
        base_url=settings.ai_base_url,
        model=settings.ai_model,
        is_configured=bool(settings.ai_api_key),
    )


@router.put("", response_model=AIConfigResponse)
async def update_ai_config(config: AIConfigRequest):
    """Update the AI configuration. Persists to storage."""
    # Load existing config to preserve fields not being updated
    existing = load_ai_config() or {}

    # Update only provided (non-empty) fields
    if config.api_key:
        existing["api_key"] = config.api_key
    if config.base_url:
        existing["base_url"] = config.base_url
    if config.model:
        existing["model"] = config.model

    save_ai_config(existing)

    return AIConfigResponse(
        api_key_masked=_mask_api_key(existing.get("api_key", "")),
        base_url=existing.get("base_url", settings.ai_base_url),
        model=existing.get("model", settings.ai_model),
        is_configured=bool(existing.get("api_key")),
    )
