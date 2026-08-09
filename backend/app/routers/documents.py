"""Document generation and download endpoints."""

import base64
import json
import os
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

from app.services.document_generator import DocumentGeneratorService
from app.core.config import settings
from app.routers.projects import _projects

router = APIRouter()

# Document generator service
_generator = DocumentGeneratorService()

# Document storage directory
_documents_dir = Path(os.path.join(settings.storage_path, "data", "documents"))
_documents_dir.mkdir(parents=True, exist_ok=True)


def _get_project_docs_dir(project_id: str) -> Path:
    """Get or create the documents directory for a project."""
    project_dir = _documents_dir / project_id
    project_dir.mkdir(parents=True, exist_ok=True)
    return project_dir


def _save_document(project_id: str, chapter: str, doc_bytes: bytes) -> None:
    """Save a generated document to disk."""
    project_dir = _get_project_docs_dir(project_id)
    doc_path = project_dir / f"{chapter}.docx"
    doc_path.write_bytes(doc_bytes)


def _load_document(project_id: str, chapter: str) -> Optional[bytes]:
    """Load a generated document from disk."""
    doc_path = _documents_dir / project_id / f"{chapter}.docx"
    if not doc_path.exists():
        return None
    return doc_path.read_bytes()


def _list_project_documents(project_id: str) -> list[dict]:
    """List all generated documents for a project."""
    project_dir = _documents_dir / project_id
    if not project_dir.exists():
        return []
    documents = []
    for doc_path in project_dir.glob("*.docx"):
        documents.append({
            "chapter": doc_path.stem,
            "size_bytes": doc_path.stat().st_size,
        })
    return documents


class GenerateDocumentRequest(BaseModel):
    """Request body for document generation."""
    content: str
    author: Optional[str] = None
    references: Optional[list[str]] = None


@router.post("/{project_id}/generate/{chapter}")
async def generate_document(
    project_id: str, chapter: str, request: GenerateDocumentRequest
):
    """Generate an APA 7 formatted document for a chapter."""
    if project_id not in _projects:
        raise HTTPException(status_code=404, detail="Project not found")

    project = _projects[project_id]
    title = f"{chapter.replace('_', ' ').title()} - {project.title or 'Investigacion'}"

    try:
        doc_bytes = _generator.create_document(
            title=title,
            content=request.content,
            author=request.author,
            references=request.references,
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error generating document: {str(e)}"
        )

    # Persist the generated document to disk
    _save_document(project_id, chapter, doc_bytes)

    return {
        "message": f"Document generated successfully for chapter: {chapter}",
        "chapter": chapter,
        "size_bytes": len(doc_bytes),
    }


@router.get("/{project_id}/download/{chapter}")
async def download_document(project_id: str, chapter: str):
    """Download a generated document."""
    doc_bytes = _load_document(project_id, chapter)
    if doc_bytes is None:
        raise HTTPException(
            status_code=404, detail=f"Document not found for chapter: {chapter}"
        )

    filename = f"{chapter}.docx"

    return Response(
        content=doc_bytes,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


@router.get("/{project_id}/list")
async def list_documents(project_id: str):
    """List all generated documents for a project."""
    documents = _list_project_documents(project_id)
    return {"documents": documents}
