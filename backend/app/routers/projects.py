"""CRUD endpoints for research projects."""

from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.models.research_project import ResearchProject, ProjectStatus
from app.services.persistence import PersistenceService

router = APIRouter()

# Persistence service
_persistence = PersistenceService()

# In-memory storage backed by file persistence
_projects: dict[str, ResearchProject] = {}


def _load_projects_from_disk():
    """Load persisted projects into memory on startup."""
    saved = _persistence.load_all_projects()
    for project_id, data in saved.items():
        try:
            _projects[project_id] = ResearchProject.model_validate(data)
        except Exception:
            continue


# Load on module import
_load_projects_from_disk()


def _persist_project(project: ResearchProject):
    """Save project to disk."""
    _persistence.save_project(project.id, project.model_dump(mode="json"))


class CreateProjectRequest(BaseModel):
    """Request body for creating a new project."""
    title: Optional[str] = None
    description: Optional[str] = None


class UpdateProjectRequest(BaseModel):
    """Request body for updating a project."""
    title: Optional[str] = None
    status: Optional[ProjectStatus] = None


@router.post("/", response_model=ResearchProject)
async def create_project(request: CreateProjectRequest):
    """Create a new research project."""
    project = ResearchProject(title=request.title, description=request.description)
    _projects[project.id] = project
    _persist_project(project)
    return project


@router.get("/", response_model=list[ResearchProject])
async def list_projects():
    """List all research projects."""
    return list(_projects.values())


@router.get("/{project_id}", response_model=ResearchProject)
async def get_project(project_id: str):
    """Get a specific research project."""
    project = _projects.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.put("/{project_id}", response_model=ResearchProject)
async def update_project(project_id: str, request: UpdateProjectRequest):
    """Update a research project."""
    project = _projects.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if request.title is not None:
        project.title = request.title
    if request.status is not None:
        project.status = request.status
    project.updated_at = datetime.utcnow()

    _projects[project_id] = project
    _persist_project(project)
    return project


@router.delete("/{project_id}")
async def delete_project(project_id: str):
    """Delete a research project."""
    if project_id not in _projects:
        raise HTTPException(status_code=404, detail="Project not found")
    del _projects[project_id]
    _persistence.delete_project(project_id)
    _persistence.delete_workflow(project_id)
    return {"message": "Project deleted successfully"}
