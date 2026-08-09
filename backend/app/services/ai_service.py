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


class AIService:
    """Multi-backend AI service using OpenAI-compatible API."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: Optional[str] = None,
    ):
        self.api_key = api_key or settings.ai_api_key
        self.base_url = base_url or settings.ai_base_url
        self.model = model or settings.ai_model
        self._client: Optional[OpenAI] = None

    @property
    def client(self) -> OpenAI:
        """Lazy-initialize the OpenAI client with API key validation."""
        if self._client is None:
            if not self.api_key:
                raise AIServiceConfigError(
                    "AI_API_KEY is not configured. Set the AI_API_KEY environment variable "
                    "or add it to your .env file to enable AI features."
                )
            self._client = OpenAI(
                api_key=self.api_key,
                base_url=self.base_url,
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
