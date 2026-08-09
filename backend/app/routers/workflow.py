"""Workflow endpoints for managing the research process."""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.models.workflow import WorkflowState, WorkflowPhase
from app.models.research_project import ResearchProject, RefinedProblem
from app.services.workflow_engine import WorkflowEngine
from app.services.persistence import PersistenceService
from app.routers.projects import _projects, _persist_project

router = APIRouter()

# Persistence service
_persistence = PersistenceService()

# In-memory workflow states backed by file persistence
_workflow_states: dict[str, WorkflowState] = {}


def _load_workflows_from_disk():
    """Load persisted workflow states into memory on startup."""
    saved = _persistence.load_all_workflows()
    for project_id, data in saved.items():
        try:
            _workflow_states[project_id] = WorkflowState.model_validate(data)
        except Exception:
            continue


# Load on module import
_load_workflows_from_disk()

# Workflow engine instance
_engine = WorkflowEngine()


def _persist_workflow(state: WorkflowState):
    """Save workflow state to disk."""
    _persistence.save_workflow(state.project_id, state.model_dump(mode="json"))


class SubmitInputRequest(BaseModel):
    """Request body for submitting input to current phase."""
    text: str
    file_content: Optional[str] = None


class SelectOptionRequest(BaseModel):
    """Request body for selecting an option (e.g., one of 3 problem formulations)."""
    option_index: int
    option_data: Optional[dict] = None


def _get_or_create_workflow(project_id: str) -> WorkflowState:
    """Get existing workflow state or create a new one."""
    if project_id not in _projects:
        raise HTTPException(status_code=404, detail="Project not found")
    if project_id not in _workflow_states:
        _workflow_states[project_id] = _engine.initialize_workflow(project_id)
        _persist_workflow(_workflow_states[project_id])
    return _workflow_states[project_id]


@router.get("/{project_id}/status")
async def get_workflow_status(project_id: str):
    """Get current workflow status for a project."""
    state = _get_or_create_workflow(project_id)
    phase_info = _engine.get_phase_description(state.current_phase)

    return {
        "project_id": project_id,
        "current_phase": state.current_phase.value,
        "phase_info": phase_info,
        "completed_phases": [p.value for p in state.completed_phases],
        "current_tasks": [
            {
                "description": t.description,
                "instruction": t.instruction,
                "completed": t.completed,
            }
            for t in state.current_tasks
        ],
        "coherence_validated": state.coherence_validated,
        "can_advance": state.can_advance(),
    }


@router.post("/{project_id}/submit-input")
async def submit_input(project_id: str, request: SubmitInputRequest):
    """Submit text/file input for the current workflow phase."""
    state = _get_or_create_workflow(project_id)
    project = _projects[project_id]

    user_input = request.text
    if request.file_content:
        user_input += f"\n\nContenido del archivo:\n{request.file_content}"

    try:
        result = _engine.process_input(state, project, user_input)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing input: {str(e)}")

    _persist_workflow(state)
    _persist_project(project)
    return {
        "phase": state.current_phase.value,
        "result": result,
        "message": "Input processed successfully",
    }


@router.post("/{project_id}/advance")
async def advance_workflow(project_id: str):
    """Advance to the next phase after validation."""
    state = _get_or_create_workflow(project_id)
    project = _projects[project_id]

    # Check state-of-art phase specific constraint
    if state.current_phase == WorkflowPhase.STATE_OF_ART:
        if not _engine.can_advance_state_of_art(project):
            raise HTTPException(
                status_code=400,
                detail=(
                    "Cannot advance: need at least 6 similar studies, or check "
                    "'no more studies found' if fewer exist."
                ),
            )

    if not state.coherence_validated:
        # Attempt validation
        validation = _engine.validate_phase_coherence(state, project)
        if not validation["is_coherent"]:
            _persist_workflow(state)
            raise HTTPException(
                status_code=400,
                detail=f"Cannot advance: coherence validation failed. {validation['message']}",
            )

    new_phase = _engine.advance_phase(state)
    if not new_phase:
        raise HTTPException(
            status_code=400,
            detail="Cannot advance: already at the last phase or validation pending",
        )

    _persist_workflow(state)
    phase_info = _engine.get_phase_description(new_phase)
    return {
        "new_phase": new_phase.value,
        "phase_info": phase_info,
        "message": f"Advanced to: {phase_info['title']}",
    }


@router.post("/{project_id}/select-option")
async def select_option(project_id: str, request: SelectOptionRequest):
    """Select from AI-generated options (e.g., problem formulations)."""
    state = _get_or_create_workflow(project_id)
    project = _projects[project_id]

    if state.current_phase == WorkflowPhase.PROBLEM_REFINEMENT:
        if project.refined_problems and request.option_index < len(
            project.refined_problems
        ):
            selected = project.refined_problems[request.option_index]
            selected.selected = True
            project.selected_problem = selected
            _persist_project(project)
            return {"message": "Problem formulation selected", "selected": selected}
        else:
            raise HTTPException(
                status_code=400, detail="Invalid option index for problem refinement"
            )

    return {"message": "Option selection recorded", "option_index": request.option_index}


@router.post("/{project_id}/validate")
async def validate_coherence(project_id: str):
    """Manually trigger coherence validation for the current phase."""
    state = _get_or_create_workflow(project_id)
    project = _projects[project_id]

    validation = _engine.validate_phase_coherence(state, project)
    _persist_workflow(state)
    return {
        "phase": state.current_phase.value,
        "is_coherent": validation["is_coherent"],
        "message": validation["message"],
    }


class AddStudyRequest(BaseModel):
    """Request body for adding a similar study to the state-of-art matrix."""
    title: str
    authors: str
    year: int
    methodology: str
    findings: str
    relevance: str
    source: Optional[str] = None


class SetNoMoreStudiesRequest(BaseModel):
    """Request body for setting the 'no more studies' flag."""
    no_more_studies_found: bool


@router.post("/{project_id}/state-of-art/add-study")
async def add_study(project_id: str, request: AddStudyRequest):
    """Add a similar study to the state-of-art matrix."""
    state = _get_or_create_workflow(project_id)
    project = _projects[project_id]

    if state.current_phase != WorkflowPhase.STATE_OF_ART:
        raise HTTPException(
            status_code=400,
            detail="Can only add studies during the state-of-art phase",
        )

    from app.models.research_project import SimilarStudy
    study = SimilarStudy(
        title=request.title,
        authors=request.authors,
        year=request.year,
        methodology=request.methodology,
        findings=request.findings,
        relevance=request.relevance,
        source=request.source,
    )
    result = _engine.add_similar_study(project, study)
    _persist_project(project)
    return {
        "message": "Study added successfully",
        **result,
    }


@router.post("/{project_id}/state-of-art/no-more-studies")
async def set_no_more_studies(project_id: str, request: SetNoMoreStudiesRequest):
    """Set the 'no more studies found' flag to allow advancing with fewer than 6 studies."""
    state = _get_or_create_workflow(project_id)
    project = _projects[project_id]

    if state.current_phase != WorkflowPhase.STATE_OF_ART:
        raise HTTPException(
            status_code=400,
            detail="Can only set this flag during the state-of-art phase",
        )

    result = _engine.set_no_more_studies(project, state, request.no_more_studies_found)
    _persist_project(project)
    _persist_workflow(state)
    return {
        "message": "Flag updated successfully",
        **result,
    }
