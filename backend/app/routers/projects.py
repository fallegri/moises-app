"""CRUD endpoints for research projects."""

from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.models.research_project import ResearchProject, ProjectStatus

router = APIRouter()

# In-memory storage (to be replaced with database in production)
_projects: dict[str, ResearchProject] = {}


class CreateProjectRequest(BaseModel):
    """Request body for creating a new project."""
    title: Optional[str] = None


class UpdateProjectRequest(BaseModel):
    """Request body for updating a project."""
    title: Optional[str] = None
    status: Optional[ProjectStatus] = None


@router.post("/", response_model=ResearchProject)
async def create_project(request: CreateProjectRequest):
    """Create a new research project."""
    project = ResearchProject(title=request.title)
    _projects[project.id] = project
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
    return project


@router.delete("/{project_id}")
async def delete_project(project_id: str):
    """Delete a research project."""
    if project_id not in _projects:
        raise HTTPException(status_code=404, detail="Project not found")
    del _projects[project_id]
    return {"message": "Project deleted successfully"}
