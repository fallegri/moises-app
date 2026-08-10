"""Tests for AI service with mocked responses."""

import pytest
from unittest.mock import MagicMock, patch, PropertyMock

from app.services.ai_service import AIService, AIServiceConfigError


@pytest.fixture
def mock_openai_response():
    """Create a mock OpenAI response."""
    mock_response = MagicMock()
    mock_choice = MagicMock()
    mock_choice.message.content = "AI response content"
    mock_response.choices = [mock_choice]
    return mock_response


@pytest.fixture
def ai_service(mock_openai_response):
    """Create an AI service with mocked client."""
    with patch("app.services.ai_service.OpenAI") as mock_openai_class, \
         patch("app.services.ai_service._get_runtime_ai_config", return_value=None):
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = mock_openai_response
        mock_client.api_key = "test-key"
        mock_client.base_url = "https://integrate.api.nvidia.com/v1"
        mock_openai_class.return_value = mock_client

        service = AIService(
            api_key="test-key",
            base_url="https://integrate.api.nvidia.com/v1",
            model="meta/llama-3.1-405b-instruct",
        )
        # Force the lazy client to initialize with our mock
        service._client = mock_client
        return service


class TestAIService:
    """Tests for AIService."""

    def test_initialization_with_defaults(self):
        """Test AI service initializes with default config."""
        with patch("app.services.ai_service.OpenAI"), \
             patch("app.services.ai_service._get_runtime_ai_config", return_value=None):
            service = AIService(api_key="test-key")
            assert service.api_key == "test-key"
            assert "nvidia" in service.base_url or service.base_url != ""

    def test_initialization_with_custom_params(self):
        """Test AI service initializes with custom parameters."""
        with patch("app.services.ai_service.OpenAI"), \
             patch("app.services.ai_service._get_runtime_ai_config", return_value=None):
            service = AIService(
                api_key="custom-key",
                base_url="http://localhost:11434/v1",
                model="llama2",
            )
            assert service.api_key == "custom-key"
            assert service.base_url == "http://localhost:11434/v1"
            assert service.model == "llama2"

    def test_analyze_problem(self, ai_service):
        """Test analyze_problem method."""
        result = ai_service.analyze_problem(
            "En la empresa hay alta rotacion de personal",
            knowledge_context="Metodologia de investigacion",
        )
        assert result == "AI response content"
        ai_service.client.chat.completions.create.assert_called_once()

        call_args = ai_service.client.chat.completions.create.call_args
        messages = call_args[1]["messages"]
        assert len(messages) == 2
        assert messages[0]["role"] == "system"
        assert messages[1]["role"] == "user"
        assert "rotacion de personal" in messages[1]["content"]

    def test_suggest_instruments(self, ai_service):
        """Test suggest_instruments method."""
        result = ai_service.suggest_instruments(
            "Problema de rotacion de personal",
            knowledge_context="Instrumentos de recopilacion",
        )
        assert result == "AI response content"
        ai_service.client.chat.completions.create.assert_called_once()

    def test_refine_problem(self, ai_service):
        """Test refine_problem method."""
        result = ai_service.refine_problem(
            problem_description="Alta rotacion",
            instrument_data="Encuesta: 80% insatisfechos",
            knowledge_context="Metodo cientifico",
        )
        assert result == "AI response content"

        call_args = ai_service.client.chat.completions.create.call_args
        messages = call_args[1]["messages"]
        assert "Alta rotacion" in messages[1]["content"]
        assert "80% insatisfechos" in messages[1]["content"]

    def test_generate_research_questions(self, ai_service):
        """Test generate_research_questions method."""
        result = ai_service.generate_research_questions(
            "La alta rotacion de personal afecta la productividad",
            knowledge_context="Formulacion de preguntas",
        )
        assert result == "AI response content"

    def test_validate_coherence(self, ai_service):
        """Test validate_coherence method."""
        result = ai_service.validate_coherence(
            phase_name="research_question",
            current_data="Como afecta la rotacion?",
            previous_data="Problema: Alta rotacion de personal",
            knowledge_context="Coherencia metodologica",
        )
        assert result == "AI response content"

        call_args = ai_service.client.chat.completions.create.call_args
        messages = call_args[1]["messages"]
        assert "research_question" in messages[1]["content"]

    def test_generate_chapter(self, ai_service):
        """Test generate_chapter method."""
        result = ai_service.generate_chapter(
            chapter_name="introduction",
            chapter_data="Datos de la introduccion",
            project_context="Contexto del proyecto",
            knowledge_context="Formato APA 7",
        )
        assert result == "AI response content"

        call_args = ai_service.client.chat.completions.create.call_args
        messages = call_args[1]["messages"]
        assert "introduction" in messages[1]["content"]
        assert "Datos de la introduccion" in messages[1]["content"]

    def test_call_ai_uses_correct_model(self, ai_service):
        """Test that API calls use the configured model."""
        ai_service.analyze_problem("test input")

        call_args = ai_service.client.chat.completions.create.call_args
        assert call_args[1]["model"] == "meta/llama-3.1-405b-instruct"

    def test_call_ai_temperature_and_max_tokens(self, ai_service):
        """Test that API calls use proper temperature and max_tokens."""
        ai_service.analyze_problem("test input")

        call_args = ai_service.client.chat.completions.create.call_args
        assert call_args[1]["temperature"] == 0.7
        assert call_args[1]["max_tokens"] == 4096

    def test_openai_compatible_endpoint(self):
        """Test that the service works with any OpenAI-compatible endpoint."""
        with patch("app.services.ai_service.OpenAI") as mock_openai_class, \
             patch("app.services.ai_service._get_runtime_ai_config", return_value=None):
            # Test with NVIDIA endpoint - client is lazy, so access .client to trigger init
            service = AIService(api_key="key", base_url="https://integrate.api.nvidia.com/v1")
            mock_openai_class.return_value.api_key = "key"
            mock_openai_class.return_value.base_url = "https://integrate.api.nvidia.com/v1"
            _ = service.client
            mock_openai_class.assert_called_with(
                api_key="key",
                base_url="https://integrate.api.nvidia.com/v1",
            )

            mock_openai_class.reset_mock()

            # Test with local Ollama endpoint
            service2 = AIService(api_key="key", base_url="http://localhost:11434/v1")
            mock_openai_class.return_value.api_key = "key"
            mock_openai_class.return_value.base_url = "http://localhost:11434/v1"
            _ = service2.client
            mock_openai_class.assert_called_with(
                api_key="key",
                base_url="http://localhost:11434/v1",
            )

    def test_missing_api_key_raises_config_error(self):
        """Test that accessing client without API key raises AIServiceConfigError."""
        with patch("app.services.ai_service._get_runtime_ai_config", return_value=None):
            service = AIService(api_key="", base_url="https://integrate.api.nvidia.com/v1")
            with pytest.raises(AIServiceConfigError, match="AI API key is not configured"):
                _ = service.client
