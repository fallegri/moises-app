"""Persistence service with factory pattern for JSON or PostgreSQL backends."""

import json
import os
from pathlib import Path
from typing import Any, Optional

from app.core.config import settings


class JsonPersistenceService:
    """File-based JSON persistence service.

    Saves data to a data/ directory with separate files for projects
    and workflow states.
    """

    def __init__(self, data_dir: Optional[str] = None):
        self.data_dir = Path(data_dir or os.path.join(settings.storage_path, "data"))
        self._ensure_dirs()

    def _ensure_dirs(self):
        """Ensure the data directory structure exists."""
        self.data_dir.mkdir(parents=True, exist_ok=True)
        (self.data_dir / "projects").mkdir(exist_ok=True)
        (self.data_dir / "workflows").mkdir(exist_ok=True)

    def save_project(self, project_id: str, project_data: dict[str, Any]) -> None:
        """Save a project to disk."""
        filepath = self.data_dir / "projects" / f"{project_id}.json"
        filepath.write_text(json.dumps(project_data, default=str, ensure_ascii=False), encoding="utf-8")

    def load_project(self, project_id: str) -> Optional[dict[str, Any]]:
        """Load a project from disk."""
        filepath = self.data_dir / "projects" / f"{project_id}.json"
        if not filepath.exists():
            return None
        return json.loads(filepath.read_text(encoding="utf-8"))

    def delete_project(self, project_id: str) -> None:
        """Delete a project file from disk."""
        filepath = self.data_dir / "projects" / f"{project_id}.json"
        if filepath.exists():
            filepath.unlink()

    def load_all_projects(self) -> dict[str, dict[str, Any]]:
        """Load all projects from disk."""
        projects = {}
        projects_dir = self.data_dir / "projects"
        if not projects_dir.exists():
            return projects
        for filepath in projects_dir.glob("*.json"):
            try:
                data = json.loads(filepath.read_text(encoding="utf-8"))
                project_id = filepath.stem
                projects[project_id] = data
            except (json.JSONDecodeError, OSError):
                continue
        return projects

    def save_workflow(self, project_id: str, workflow_data: dict[str, Any]) -> None:
        """Save a workflow state to disk."""
        filepath = self.data_dir / "workflows" / f"{project_id}.json"
        filepath.write_text(json.dumps(workflow_data, default=str, ensure_ascii=False), encoding="utf-8")

    def load_workflow(self, project_id: str) -> Optional[dict[str, Any]]:
        """Load a workflow state from disk."""
        filepath = self.data_dir / "workflows" / f"{project_id}.json"
        if not filepath.exists():
            return None
        return json.loads(filepath.read_text(encoding="utf-8"))

    def delete_workflow(self, project_id: str) -> None:
        """Delete a workflow state file from disk."""
        filepath = self.data_dir / "workflows" / f"{project_id}.json"
        if filepath.exists():
            filepath.unlink()

    def load_all_workflows(self) -> dict[str, dict[str, Any]]:
        """Load all workflow states from disk."""
        workflows = {}
        workflows_dir = self.data_dir / "workflows"
        if not workflows_dir.exists():
            return workflows
        for filepath in workflows_dir.glob("*.json"):
            try:
                data = json.loads(filepath.read_text(encoding="utf-8"))
                project_id = filepath.stem
                workflows[project_id] = data
            except (json.JSONDecodeError, OSError):
                continue
        return workflows

    def save_ai_config(self, config: dict[str, Any]) -> None:
        """Save AI configuration to a JSON file."""
        config_file = Path(settings.storage_path) / "ai_config.json"
        config_file.parent.mkdir(parents=True, exist_ok=True)
        config_file.write_text(
            json.dumps(config, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def load_ai_config(self) -> Optional[dict[str, Any]]:
        """Load AI configuration from a JSON file."""
        config_file = Path(settings.storage_path) / "ai_config.json"
        if not config_file.exists():
            return None
        try:
            return json.loads(config_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return None


# Keep backward compatibility alias
PersistenceService = JsonPersistenceService


def get_persistence_service():
    """Factory function that returns the appropriate persistence service.

    Returns PostgresPersistenceService if DATABASE_URL is configured,
    otherwise returns JsonPersistenceService.
    """
    if settings.database_url:
        from app.services.persistence_postgres import PostgresPersistenceService
        return PostgresPersistenceService()
    return JsonPersistenceService()
