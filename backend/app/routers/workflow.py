"""Workflow endpoints for managing the research process."""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.models.workflow import WorkflowState, WorkflowPhase
from app.models.research_project import ResearchProject, RefinedProblem
from app.services.workflow_engine import WorkflowEngine
from app.routers.projects import _projects

router = APIRouter()

# In-memory workflow states
_workflow_states: dict[str, WorkflowState] = {}

# Workflow engine instance
_engine = WorkflowEngine()


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

    return {
        "phase": state.current_phase.value,
        "result": result,
        "message": "Input processed successfully",
    }


@router.post("/{project_id}/advance")
async def advance_workflow(project_id: str):
    """Advance to the next phase after validation."""
    state = _get_or_create_workflow(project_id)

    if not state.coherence_validated:
        # Attempt validation
        project = _projects[project_id]
        validation = _engine.validate_phase_coherence(state, project)
        if not validation["is_coherent"]:
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
    return {
        "phase": state.current_phase.value,
        "is_coherent": validation["is_coherent"],
        "message": validation["message"],
    }
