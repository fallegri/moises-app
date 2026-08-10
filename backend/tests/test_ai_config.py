"""Tests for AI configuration endpoints."""

import json
import shutil
import pytest
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app
from app.routers.ai_config import load_ai_config, save_ai_config, _mask_api_key


@pytest.fixture(autouse=True)
def clean_config(tmp_path, monkeypatch):
    """Use a temporary config file for each test."""
    config_file = tmp_path / "ai_config.json"
    monkeypatch.setattr("app.routers.ai_config._CONFIG_FILE", config_file)
    yield config_file


@pytest.fixture
def client():
    """Create a test client."""
    return TestClient(app)


class TestMaskApiKey:
    """Tests for the _mask_api_key utility function."""

    def test_mask_long_key(self):
        # "sk-abc123def456" has 15 chars, so 11 asterisks + last 4
        assert _mask_api_key("sk-abc123def456") == "***********f456"

    def test_mask_short_key(self):
        assert _mask_api_key("abcd") == "****"

    def test_mask_empty_key(self):
        assert _mask_api_key("") == ""

    def test_mask_5_char_key(self):
        assert _mask_api_key("12345") == "*2345"


class TestAIConfigEndpoints:
    """Tests for the /api/ai-config endpoints."""

    def test_get_config_no_file(self, client, clean_config):
        """GET returns default config when no file exists."""
        response = client.get("/api/ai-config")
        assert response.status_code == 200
        data = response.json()
        assert "api_key_masked" in data
        assert "base_url" in data
        assert "model" in data
        assert "is_configured" in data

    def test_put_config_saves(self, client, clean_config):
        """PUT saves config and returns masked response."""
        response = client.put(
            "/api/ai-config",
            json={
                "api_key": "sk-test-1234567890abcdef",
                "base_url": "https://api.openai.com/v1",
                "model": "gpt-4",
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert data["api_key_masked"] == "********************cdef"
        assert data["base_url"] == "https://api.openai.com/v1"
        assert data["model"] == "gpt-4"
        assert data["is_configured"] is True

        # Verify file was written
        assert clean_config.exists()
        saved = json.loads(clean_config.read_text())
        assert saved["api_key"] == "sk-test-1234567890abcdef"

    def test_get_config_after_save(self, client, clean_config):
        """GET returns saved config after PUT."""
        # First save
        client.put(
            "/api/ai-config",
            json={
                "api_key": "nvapi-my-test-key-1234",
                "base_url": "https://integrate.api.nvidia.com/v1",
                "model": "meta/llama-3.1-405b-instruct",
            },
        )
        # Then retrieve
        response = client.get("/api/ai-config")
        assert response.status_code == 200
        data = response.json()
        assert data["api_key_masked"] == "******************1234"
        assert data["is_configured"] is True
        assert data["base_url"] == "https://integrate.api.nvidia.com/v1"

    def test_put_partial_update(self, client, clean_config):
        """PUT with partial fields only updates provided fields."""
        # First save complete config
        client.put(
            "/api/ai-config",
            json={
                "api_key": "sk-original-key-12345678",
                "base_url": "https://api.openai.com/v1",
                "model": "gpt-4",
            },
        )
        # Update only model (empty strings for other fields)
        response = client.put(
            "/api/ai-config",
            json={"api_key": "", "base_url": "", "model": "gpt-4o"},
        )
        assert response.status_code == 200
        data = response.json()
        # api_key should remain from first save
        assert data["is_configured"] is True
        assert data["model"] == "gpt-4o"
        assert data["base_url"] == "https://api.openai.com/v1"


class TestLoadSaveConfig:
    """Tests for the load/save utility functions."""

    def test_load_nonexistent(self, clean_config):
        """load_ai_config returns None if file does not exist."""
        result = load_ai_config()
        assert result is None

    def test_save_and_load(self, clean_config, monkeypatch):
        """save_ai_config persists data that load_ai_config can read."""
        monkeypatch.setattr("app.routers.ai_config._CONFIG_FILE", clean_config)
        save_ai_config({"api_key": "test123", "base_url": "http://x", "model": "m"})
        result = load_ai_config()
        assert result["api_key"] == "test123"
        assert result["base_url"] == "http://x"
        assert result["model"] == "m"
