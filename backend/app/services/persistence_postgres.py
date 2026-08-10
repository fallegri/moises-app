"""PostgreSQL-based persistence service using synchronous SQLAlchemy."""

import json
import logging
from datetime import datetime
from typing import Any, Optional

from app.db.session import get_session
from app.db.models import ResearchProjectDB, WorkflowStateDB, AIConfigDB

logger = logging.getLogger(__name__)


class PostgresPersistenceService:
    """PostgreSQL persistence service.

    Uses synchronous SQLAlchemy sessions with psycopg2 driver.
    Implements the same interface as JsonPersistenceService.
    """

    def save_project(self, project_id: str, project_data: dict[str, Any]) -> None:
        """Save a project to PostgreSQL."""
        session = get_session()
        try:
            existing = session.get(ResearchProjectDB, project_id)
            if existing:
                existing.title = project_data.get("title")
                existing.description = project_data.get("description")
                existing.status = project_data.get("status", "active")
                existing.created_at = _parse_datetime(project_data.get("created_at"))
                existing.updated_at = _parse_datetime(project_data.get("updated_at"))
                existing.problem_description = project_data.get("problem_description")
                existing.suggested_instruments = project_data.get("suggested_instruments", [])
                existing.refined_problems = project_data.get("refined_problems", [])
                existing.selected_problem = project_data.get("selected_problem")
                existing.research_question = project_data.get("research_question")
                existing.introduction = project_data.get("introduction")
                existing.state_of_art = project_data.get("state_of_art", {})
                existing.specific_problems = project_data.get("specific_problems", [])
                existing.research_objective = project_data.get("research_objective")
                existing.specific_objectives = project_data.get("specific_objectives", [])
                existing.methodological_framework = project_data.get("methodological_framework", {})
                existing.additional_literature = project_data.get("additional_literature", [])
            else:
                db_project = ResearchProjectDB(
                    id=project_id,
                    title=project_data.get("title"),
                    description=project_data.get("description"),
                    status=project_data.get("status", "active"),
                    created_at=_parse_datetime(project_data.get("created_at")),
                    updated_at=_parse_datetime(project_data.get("updated_at")),
                    problem_description=project_data.get("problem_description"),
                    suggested_instruments=project_data.get("suggested_instruments", []),
                    refined_problems=project_data.get("refined_problems", []),
                    selected_problem=project_data.get("selected_problem"),
                    research_question=project_data.get("research_question"),
                    introduction=project_data.get("introduction"),
                    state_of_art=project_data.get("state_of_art", {}),
                    specific_problems=project_data.get("specific_problems", []),
                    research_objective=project_data.get("research_objective"),
                    specific_objectives=project_data.get("specific_objectives", []),
                    methodological_framework=project_data.get("methodological_framework", {}),
                    additional_literature=project_data.get("additional_literature", []),
                )
                session.add(db_project)
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def load_project(self, project_id: str) -> Optional[dict[str, Any]]:
        """Load a project from PostgreSQL."""
        session = get_session()
        try:
            db_project = session.get(ResearchProjectDB, project_id)
            if db_project is None:
                return None
            return _project_db_to_dict(db_project)
        finally:
            session.close()

    def delete_project(self, project_id: str) -> None:
        """Delete a project from PostgreSQL."""
        session = get_session()
        try:
            db_project = session.get(ResearchProjectDB, project_id)
            if db_project:
                session.delete(db_project)
                session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def load_all_projects(self) -> dict[str, dict[str, Any]]:
        """Load all projects from PostgreSQL."""
        session = get_session()
        try:
            projects = session.query(ResearchProjectDB).all()
            return {p.id: _project_db_to_dict(p) for p in projects}
        finally:
            session.close()

    def save_workflow(self, project_id: str, workflow_data: dict[str, Any]) -> None:
        """Save a workflow state to PostgreSQL."""
        session = get_session()
        try:
            existing = session.get(WorkflowStateDB, project_id)
            if existing:
                existing.current_phase = workflow_data.get("current_phase", "problem_identification")
                existing.completed_phases = workflow_data.get("completed_phases", [])
                existing.current_tasks = workflow_data.get("current_tasks", [])
                existing.phase_data = workflow_data.get("phase_data", {})
                existing.coherence_validated = bool(workflow_data.get("coherence_validated", False))
                existing.last_validation_message = workflow_data.get("last_validation_message")
                existing.updated_at = _parse_datetime(workflow_data.get("updated_at"))
            else:
                db_workflow = WorkflowStateDB(
                    project_id=project_id,
                    current_phase=workflow_data.get("current_phase", "problem_identification"),
                    completed_phases=workflow_data.get("completed_phases", []),
                    current_tasks=workflow_data.get("current_tasks", []),
                    phase_data=workflow_data.get("phase_data", {}),
                    coherence_validated=bool(workflow_data.get("coherence_validated", False)),
                    last_validation_message=workflow_data.get("last_validation_message"),
                    updated_at=_parse_datetime(workflow_data.get("updated_at")),
                )
                session.add(db_workflow)
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def load_workflow(self, project_id: str) -> Optional[dict[str, Any]]:
        """Load a workflow state from PostgreSQL."""
        session = get_session()
        try:
            db_workflow = session.get(WorkflowStateDB, project_id)
            if db_workflow is None:
                return None
            return _workflow_db_to_dict(db_workflow)
        finally:
            session.close()

    def delete_workflow(self, project_id: str) -> None:
        """Delete a workflow state from PostgreSQL."""
        session = get_session()
        try:
            db_workflow = session.get(WorkflowStateDB, project_id)
            if db_workflow:
                session.delete(db_workflow)
                session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def load_all_workflows(self) -> dict[str, dict[str, Any]]:
        """Load all workflow states from PostgreSQL."""
        session = get_session()
        try:
            workflows = session.query(WorkflowStateDB).all()
            return {w.project_id: _workflow_db_to_dict(w) for w in workflows}
        finally:
            session.close()

    def save_ai_config(self, config: dict[str, Any]) -> None:
        """Save AI configuration to PostgreSQL."""
        session = get_session()
        try:
            existing = session.get(AIConfigDB, "default")
            if existing:
                existing.config_data = config
                existing.updated_at = datetime.utcnow()
            else:
                db_config = AIConfigDB(
                    id="default",
                    config_data=config,
                    updated_at=datetime.utcnow(),
                )
                session.add(db_config)
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def load_ai_config(self) -> Optional[dict[str, Any]]:
        """Load AI configuration from PostgreSQL."""
        session = get_session()
        try:
            db_config = session.get(AIConfigDB, "default")
            if db_config is None:
                return None
            return db_config.config_data
        except Exception:
            return None
        finally:
            session.close()


def _parse_datetime(value) -> datetime:
    """Parse a datetime value from various formats.

    Logs a warning when parsing fails and falls back to the current UTC time.
    """
    if value is None:
        return datetime.utcnow()
    if isinstance(value, datetime):
        return value
    if isinstance(value, str):
        try:
            return datetime.fromisoformat(value.replace("Z", "+00:00"))
        except (ValueError, TypeError):
            logger.warning(
                "Failed to parse datetime value %r; falling back to utcnow()",
                value,
            )
            return datetime.utcnow()
    logger.warning(
        "Unexpected datetime type %s for value %r; falling back to utcnow()",
        type(value).__name__,
        value,
    )
    return datetime.utcnow()


def _project_db_to_dict(db_project: ResearchProjectDB) -> dict[str, Any]:
    """Convert a database project record to a dictionary."""
    return {
        "id": db_project.id,
        "title": db_project.title,
        "description": db_project.description,
        "status": db_project.status,
        "created_at": db_project.created_at.isoformat() if db_project.created_at else None,
        "updated_at": db_project.updated_at.isoformat() if db_project.updated_at else None,
        "problem_description": db_project.problem_description,
        "suggested_instruments": db_project.suggested_instruments or [],
        "refined_problems": db_project.refined_problems or [],
        "selected_problem": db_project.selected_problem,
        "research_question": db_project.research_question,
        "introduction": db_project.introduction,
        "state_of_art": db_project.state_of_art or {"studies": [], "no_more_studies_found": False, "synthesis": None},
        "specific_problems": db_project.specific_problems or [],
        "research_objective": db_project.research_objective,
        "specific_objectives": db_project.specific_objectives or [],
        "methodological_framework": db_project.methodological_framework or {},
        "additional_literature": db_project.additional_literature or [],
    }


def _workflow_db_to_dict(db_workflow: WorkflowStateDB) -> dict[str, Any]:
    """Convert a database workflow record to a dictionary."""
    return {
        "project_id": db_workflow.project_id,
        "current_phase": db_workflow.current_phase,
        "completed_phases": db_workflow.completed_phases or [],
        "current_tasks": db_workflow.current_tasks or [],
        "phase_data": db_workflow.phase_data or {},
        "coherence_validated": bool(db_workflow.coherence_validated),
        "last_validation_message": db_workflow.last_validation_message,
        "updated_at": db_workflow.updated_at.isoformat() if db_workflow.updated_at else None,
    }
