"""Workflow state tracking for the research process."""

from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, Field
from enum import Enum


class WorkflowPhase(str, Enum):
    """Research workflow phases in order."""
    PROBLEM_IDENTIFICATION = "problem_identification"
    INSTRUMENT_SUGGESTION = "instrument_suggestion"
    PROBLEM_REFINEMENT = "problem_refinement"
    RESEARCH_QUESTION = "research_question"
    INTRODUCTION = "introduction"
    STATE_OF_ART = "state_of_art"
    PROBLEM_IDENTIFICATION_CHAPTER = "problem_identification_chapter"
    SPECIFIC_PROBLEMS = "specific_problems"
    RESEARCH_OBJECTIVE = "research_objective"
    SPECIFIC_OBJECTIVES = "specific_objectives"
    METHODOLOGICAL_FRAMEWORK = "methodological_framework"
    DATA_COLLECTION_INSTRUMENTS = "data_collection_instruments"


# Ordered list of phases for progression tracking
PHASE_ORDER = [
    WorkflowPhase.PROBLEM_IDENTIFICATION,
    WorkflowPhase.INSTRUMENT_SUGGESTION,
    WorkflowPhase.PROBLEM_REFINEMENT,
    WorkflowPhase.RESEARCH_QUESTION,
    WorkflowPhase.INTRODUCTION,
    WorkflowPhase.STATE_OF_ART,
    WorkflowPhase.PROBLEM_IDENTIFICATION_CHAPTER,
    WorkflowPhase.SPECIFIC_PROBLEMS,
    WorkflowPhase.RESEARCH_OBJECTIVE,
    WorkflowPhase.SPECIFIC_OBJECTIVES,
    WorkflowPhase.METHODOLOGICAL_FRAMEWORK,
    WorkflowPhase.DATA_COLLECTION_INSTRUMENTS,
]


class PhaseTask(BaseModel):
    """A task within a workflow phase."""
    description: str
    instruction: str
    completed: bool = False
    response_data: Optional[Any] = None


class WorkflowState(BaseModel):
    """Tracks the workflow state for a research project."""
    project_id: str
    current_phase: WorkflowPhase = WorkflowPhase.PROBLEM_IDENTIFICATION
    completed_phases: list[WorkflowPhase] = Field(default_factory=list)
    current_tasks: list[PhaseTask] = Field(default_factory=list)
    phase_data: dict[str, Any] = Field(default_factory=dict)
    coherence_validated: bool = False
    last_validation_message: Optional[str] = None
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def get_phase_index(self) -> int:
        """Get the index of the current phase."""
        return PHASE_ORDER.index(self.current_phase)

    def _current_phase_submitted(self) -> bool:
        """Return True if the current phase has a stored submission.

        A phase is considered submitted when all of its current tasks are
        marked completed, or (as a fallback) when phase_data holds a result
        for the current phase. This is what gates advancement now, so a phase
        can never be permanently blocked by coherence validation.
        """
        if self.current_tasks:
            if all(task.completed for task in self.current_tasks):
                return True
        return self.current_phase.value in self.phase_data

    def can_advance(self) -> bool:
        """Check if the workflow can advance to the next phase.

        Advancement is gated on the current phase having been submitted (its
        tasks completed / phase_data populated) and not being the last phase.
        Coherence validation is ADVISORY and no longer blocks advancement.
        """
        current_idx = self.get_phase_index()
        if current_idx >= len(PHASE_ORDER) - 1:
            return False
        return self._current_phase_submitted()

    def advance_phase(self) -> Optional[WorkflowPhase]:
        """Advance to the next phase if possible."""
        if not self.can_advance():
            return None
        self.completed_phases.append(self.current_phase)
        current_idx = self.get_phase_index()
        self.current_phase = PHASE_ORDER[current_idx + 1]
        self.coherence_validated = False
        self.current_tasks = []
        self.updated_at = datetime.utcnow()
        return self.current_phase
