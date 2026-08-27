"""Tests for the workflow engine phases and transitions."""

import pytest
from unittest.mock import MagicMock, patch

from app.models.workflow import WorkflowState, WorkflowPhase, PHASE_ORDER
from app.models.research_project import ResearchProject, ProblemDescription, RefinedProblem
from app.services.workflow_engine import WorkflowEngine


@pytest.fixture
def mock_ai_service():
    """Create a mocked AI service."""
    service = MagicMock()
    service.analyze_problem.return_value = "Problema identificado: Falta de acceso a educacion en zonas rurales"
    service.suggest_instruments.return_value = (
        "1. Encuesta a habitantes\n2. Entrevista a docentes\n3. Observacion directa"
    )
    service.refine_problem.return_value = (
        "1. La escasez de instituciones educativas en zonas rurales limita el acceso a educacion.\n"
        "2. La falta de docentes capacitados en areas rurales reduce la calidad educativa.\n"
        "3. La infraestructura deficiente en zonas rurales impide el desarrollo educativo."
    )
    service.generate_research_questions.return_value = (
        "Pregunta principal: Como afecta la falta de instituciones educativas al desarrollo en zonas rurales?"
    )
    service.validate_coherence.return_value = "COHERENTE: Los datos presentan consistencia logica."
    service.generate_chapter.return_value = "Capitulo generado con formato APA 7."
    return service


@pytest.fixture
def mock_knowledge_base():
    """Create a mocked knowledge base service."""
    kb = MagicMock()
    kb.get_context_for_phase.return_value = "Contexto metodologico relevante."
    return kb


@pytest.fixture
def engine(mock_ai_service, mock_knowledge_base):
    """Create a workflow engine with mocked services."""
    return WorkflowEngine(ai_service=mock_ai_service, knowledge_base=mock_knowledge_base)


@pytest.fixture
def project():
    """Create a test research project."""
    return ResearchProject(title="Test Research Project")


class TestWorkflowState:
    """Tests for WorkflowState model."""

    def test_initial_state(self):
        """Test initial workflow state."""
        state = WorkflowState(project_id="test-123")
        assert state.current_phase == WorkflowPhase.PROBLEM_IDENTIFICATION
        assert state.completed_phases == []
        assert state.coherence_validated is False

    def test_get_phase_index(self):
        """Test phase index retrieval."""
        state = WorkflowState(project_id="test-123")
        assert state.get_phase_index() == 0

        state.current_phase = WorkflowPhase.PROBLEM_REFINEMENT
        assert state.get_phase_index() == 2

    def test_cannot_advance_without_validation(self):
        """A fresh state (nothing submitted) cannot advance.

        Advancement is now gated on the current phase being submitted (its
        tasks completed / phase_data populated), not on coherence. A fresh
        state has no submission, so can_advance() must be False. This assertion
        still holds under the new submission-based gating.
        """
        state = WorkflowState(project_id="test-123")
        assert state.can_advance() is False

    def test_can_advance_after_submission(self):
        """A phase can advance once it has been submitted.

        Coherence is now ADVISORY and no longer gates advancement. What matters
        is that the current phase's tasks are completed (i.e. the user has
        submitted). This replaces the old coherence-based gating: setting
        coherence_validated alone is no longer sufficient.
        """
        state = WorkflowState(project_id="test-123")
        # Coherence validated but nothing submitted -> still cannot advance.
        state.coherence_validated = True
        assert state.can_advance() is False

        # Mark the current phase as submitted via phase_data -> can advance,
        # even though coherence_validated is now irrelevant.
        state.coherence_validated = False
        state.phase_data[state.current_phase.value] = {"identified_problem": "x"}
        assert state.can_advance() is True

    def test_advance_phase(self):
        """Test advancing to next phase after submission."""
        state = WorkflowState(project_id="test-123")
        # Submission (not coherence) is what enables advancement now.
        state.phase_data[state.current_phase.value] = {"identified_problem": "x"}
        new_phase = state.advance_phase()

        assert new_phase == WorkflowPhase.INSTRUMENT_SUGGESTION
        assert state.current_phase == WorkflowPhase.INSTRUMENT_SUGGESTION
        assert WorkflowPhase.PROBLEM_IDENTIFICATION in state.completed_phases
        assert state.coherence_validated is False

    def test_cannot_advance_from_last_phase(self):
        """Test that cannot advance from the last phase even after submission."""
        state = WorkflowState(project_id="test-123")
        state.current_phase = WorkflowPhase.DATA_COLLECTION_INSTRUMENTS
        # Even with a submission recorded, the last phase cannot advance.
        state.phase_data[state.current_phase.value] = {"generated_content": "x"}
        assert state.can_advance() is False

    def test_phase_order_completeness(self):
        """Test that all phases are in the order list."""
        assert len(PHASE_ORDER) == 12
        assert PHASE_ORDER[0] == WorkflowPhase.PROBLEM_IDENTIFICATION
        assert PHASE_ORDER[-1] == WorkflowPhase.DATA_COLLECTION_INSTRUMENTS


class TestWorkflowEngine:
    """Tests for WorkflowEngine."""

    def test_initialize_workflow(self, engine):
        """Test workflow initialization."""
        state = engine.initialize_workflow("project-1")
        assert state.project_id == "project-1"
        assert state.current_phase == WorkflowPhase.PROBLEM_IDENTIFICATION
        assert len(state.current_tasks) > 0

    def test_process_input_problem_identification(self, engine, project):
        """Test processing input for problem identification phase."""
        state = engine.initialize_workflow(project.id)
        result = engine.process_input(
            state, project, "En mi empresa hay alta rotacion de personal"
        )

        assert "identified_problem" in result
        assert project.problem_description is not None
        assert project.problem_description.raw_text == "En mi empresa hay alta rotacion de personal"

    def test_process_input_marks_task_completed_and_stores_response(self, engine, project):
        """After submitting, the phase task is completed and the AI result is stored.

        Covers acceptance: task.completed becomes True and the AI response is
        retrievable via both task.response_data and state.phase_data.
        """
        state = engine.initialize_workflow(project.id)
        assert state.current_tasks[0].completed is False

        result = engine.process_input(state, project, "Situacion problematica")

        # Task marked completed and AI result attached per-task.
        assert state.current_tasks[0].completed is True
        assert state.current_tasks[0].response_data == result
        # Result also survives in phase_data (serialized/reloaded elsewhere).
        assert state.phase_data[WorkflowPhase.PROBLEM_IDENTIFICATION.value] == result
        assert "identified_problem" in state.phase_data[
            WorkflowPhase.PROBLEM_IDENTIFICATION.value
        ]

    def test_can_advance_true_after_submission_even_if_incoherent(
        self, engine, project, mock_ai_service
    ):
        """can_advance() is True after submission even when coherence fails.

        Coherence is advisory: a negative coherence result must not block
        advancement once the phase has been submitted.
        """
        mock_ai_service.validate_coherence.return_value = "INCOHERENTE: inconsistencias."
        state = engine.initialize_workflow(project.id)

        # Before any submission, cannot advance.
        assert state.can_advance() is False

        engine.process_input(state, project, "Situacion problematica")

        # Coherence auto-ran and reported incoherent, yet advancement is allowed.
        assert state.coherence_validated is False
        assert state.can_advance() is True

    def test_can_advance_false_on_last_phase_after_submission(self, engine, project):
        """can_advance() is False on the last phase even after a submission."""
        state = engine.initialize_workflow(project.id)
        state.current_phase = WorkflowPhase.DATA_COLLECTION_INSTRUMENTS
        state.current_tasks = engine._get_phase_tasks(state.current_phase)

        engine.process_input(state, project, "Requisitos de instrumentos")

        assert state.can_advance() is False

    def test_advance_does_not_require_coherence(self, engine, project, mock_ai_service):
        """Advancing works after a submission without a successful coherence check."""
        mock_ai_service.validate_coherence.return_value = "INCOHERENTE: inconsistencias."
        state = engine.initialize_workflow(project.id)

        engine.process_input(state, project, "Situacion problematica")
        new_phase = engine.advance_phase(state)

        assert new_phase == WorkflowPhase.INSTRUMENT_SUGGESTION

    def test_process_input_instrument_suggestion(self, engine, project):
        """Test processing input for instrument suggestion phase."""
        project.problem_description = ProblemDescription(
            raw_text="Alta rotacion",
            identified_problem="Problema de rotacion de personal",
        )
        state = engine.initialize_workflow(project.id)
        state.current_phase = WorkflowPhase.INSTRUMENT_SUGGESTION

        result = engine.process_input(state, project, "Datos adicionales")
        assert "suggested_instruments" in result

    def test_process_input_problem_refinement(self, engine, project):
        """Test processing input for problem refinement phase."""
        project.problem_description = ProblemDescription(
            raw_text="Alta rotacion",
            identified_problem="Problema de rotacion",
        )
        state = engine.initialize_workflow(project.id)
        state.current_phase = WorkflowPhase.PROBLEM_REFINEMENT

        result = engine.process_input(state, project, "Datos de encuestas")
        assert "refined_formulations" in result

    def test_validate_phase_coherence_positive(self, engine, project):
        """Test positive coherence validation."""
        state = engine.initialize_workflow(project.id)
        state.phase_data["problem_identification"] = {"identified_problem": "Test"}

        validation = engine.validate_phase_coherence(state, project)
        assert validation["is_coherent"] is True
        assert state.coherence_validated is True

    def test_validate_phase_coherence_negative(self, engine, project, mock_ai_service):
        """Test negative coherence validation."""
        mock_ai_service.validate_coherence.return_value = "INCOHERENTE: Hay inconsistencias."
        state = engine.initialize_workflow(project.id)

        validation = engine.validate_phase_coherence(state, project)
        assert validation["is_coherent"] is False
        assert state.coherence_validated is False

    def test_advance_phase_flow(self, engine, project):
        """Test advancing through multiple phases."""
        state = engine.initialize_workflow(project.id)

        # Process first phase
        engine.process_input(state, project, "Situacion problematica")
        engine.validate_phase_coherence(state, project)

        # Advance to next phase
        new_phase = engine.advance_phase(state)
        assert new_phase == WorkflowPhase.INSTRUMENT_SUGGESTION
        assert len(state.current_tasks) > 0

    def test_get_phase_description(self, engine):
        """Test getting phase descriptions."""
        desc = engine.get_phase_description(WorkflowPhase.PROBLEM_IDENTIFICATION)
        assert "title" in desc
        assert "description" in desc
        assert "instruction" in desc
        assert desc["title"] == "Identificacion del Problema"

    def test_full_workflow_progression(self, engine, project):
        """Test progressing through multiple phases."""
        state = engine.initialize_workflow(project.id)

        # Progress through first 3 phases
        for i in range(3):
            engine.process_input(state, project, f"Input for phase {i}")
            engine.validate_phase_coherence(state, project)
            engine.advance_phase(state)

        assert state.current_phase == WorkflowPhase.RESEARCH_QUESTION
        assert len(state.completed_phases) == 3
