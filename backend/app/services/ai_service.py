"""AI service supporting OpenAI-compatible endpoints."""

from typing import Optional
from openai import OpenAI

from app.core.config import settings
from app.core.prompts import (
    ANALYZE_PROBLEM_PROMPT,
    SUGGEST_INSTRUMENTS_PROMPT,
    REFINE_PROBLEM_PROMPT,
    GENERATE_RESEARCH_QUESTIONS_PROMPT,
    VALIDATE_COHERENCE_PROMPT,
    GENERATE_CHAPTER_PROMPT,
)


class AIServiceConfigError(Exception):
    """Raised when the AI service is not properly configured."""
    pass


def _get_runtime_ai_config() -> Optional[dict]:
    """Load runtime AI configuration from persistent storage.

    This is checked each time the client is initialized so that
    config changes from the UI take effect without restarting.
    """
    from app.routers.ai_config import load_ai_config
    return load_ai_config()


class AIService:
    """Multi-backend AI service using OpenAI-compatible API."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: Optional[str] = None,
    ):
        self._explicit_api_key = api_key
        self._explicit_base_url = base_url
        self._explicit_model = model
        self._client: Optional[OpenAI] = None

    def _resolve_config(self) -> tuple[str, str, str]:
        """Resolve AI configuration: explicit > runtime (UI) > .env settings."""
        runtime_config = _get_runtime_ai_config()

        api_key = self._explicit_api_key or ""
        base_url = self._explicit_base_url or ""
        model = self._explicit_model or ""

        # If not explicitly set, check runtime config from UI
        if not api_key and runtime_config:
            api_key = runtime_config.get("api_key", "")
        if not base_url and runtime_config:
            base_url = runtime_config.get("base_url", "")
        if not model and runtime_config:
            model = runtime_config.get("model", "")

        # Fall back to .env settings
        if not api_key:
            api_key = settings.ai_api_key
        if not base_url:
            base_url = settings.ai_base_url
        if not model:
            model = settings.ai_model

        return api_key, base_url, model

    @property
    def api_key(self) -> str:
        """Get the resolved API key."""
        api_key, _, _ = self._resolve_config()
        return api_key

    @property
    def base_url(self) -> str:
        """Get the resolved base URL."""
        _, base_url, _ = self._resolve_config()
        return base_url

    @property
    def model(self) -> str:
        """Get the resolved model."""
        _, _, model = self._resolve_config()
        return model

    @property
    def client(self) -> OpenAI:
        """Lazy-initialize the OpenAI client with API key validation.

        Re-creates the client if the runtime config has changed.
        """
        api_key, base_url, _ = self._resolve_config()

        if not api_key:
            raise AIServiceConfigError(
                "AI API key is not configured. Configure it in the AI Settings "
                "panel or set the AI_API_KEY environment variable."
            )

        # Re-create client if config changed
        if self._client is None or self._client.api_key != api_key or str(self._client.base_url).rstrip("/") != base_url.rstrip("/"):
            self._client = OpenAI(
                api_key=api_key,
                base_url=base_url,
            )
        return self._client

    def _call_ai(self, system_prompt: str, user_message: str) -> str:
        """Make a call to the AI API."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            temperature=0.7,
            max_tokens=4096,
        )
        return response.choices[0].message.content or ""

    def analyze_problem(
        self, situation_description: str, knowledge_context: str = ""
    ) -> str:
        """Analyze a problematic situation and identify the apparent problem."""
        system_prompt = ANALYZE_PROBLEM_PROMPT.format(
            knowledge_context=knowledge_context
        )
        return self._call_ai(system_prompt, situation_description)

    def suggest_instruments(
        self, identified_problem: str, knowledge_context: str = ""
    ) -> str:
        """Suggest instruments to better identify the problem."""
        system_prompt = SUGGEST_INSTRUMENTS_PROMPT.format(
            knowledge_context=knowledge_context
        )
        return self._call_ai(system_prompt, identified_problem)

    def refine_problem(
        self,
        problem_description: str,
        instrument_data: str,
        knowledge_context: str = "",
    ) -> str:
        """Refine the problem and offer 3 formulations using the scientific method."""
        system_prompt = REFINE_PROBLEM_PROMPT.format(
            knowledge_context=knowledge_context
        )
        user_message = (
            f"Problema identificado:\n{problem_description}\n\n"
            f"Datos recopilados con instrumentos:\n{instrument_data}"
        )
        return self._call_ai(system_prompt, user_message)

    def generate_research_questions(
        self, selected_problem: str, knowledge_context: str = ""
    ) -> str:
        """Generate research questions from the selected problem formulation."""
        system_prompt = GENERATE_RESEARCH_QUESTIONS_PROMPT.format(
            knowledge_context=knowledge_context
        )
        return self._call_ai(system_prompt, selected_problem)

    def validate_coherence(
        self,
        phase_name: str,
        current_data: str,
        previous_data: str,
        knowledge_context: str = "",
    ) -> str:
        """Validate coherence between current phase data and previous phases."""
        system_prompt = VALIDATE_COHERENCE_PROMPT.format(
            knowledge_context=knowledge_context
        )
        user_message = (
            f"Fase actual: {phase_name}\n\n"
            f"Datos actuales:\n{current_data}\n\n"
            f"Datos previos:\n{previous_data}"
        )
        return self._call_ai(system_prompt, user_message)

    def generate_chapter(
        self,
        chapter_name: str,
        chapter_data: str,
        project_context: str,
        knowledge_context: str = "",
    ) -> str:
        """Generate a chapter following APA 7 format."""
        system_prompt = GENERATE_CHAPTER_PROMPT.format(
            knowledge_context=knowledge_context
        )
        user_message = (
            f"Capitulo: {chapter_name}\n\n"
            f"Datos del capitulo:\n{chapter_data}\n\n"
            f"Contexto del proyecto:\n{project_context}"
        )
        return self._call_ai(system_prompt, user_message)
