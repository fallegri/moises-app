"""Document generation and download endpoints."""

from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from typing import Optional

from app.services.document_generator import DocumentGeneratorService
from app.routers.projects import _projects

router = APIRouter()

# Document generator service
_generator = DocumentGeneratorService()

# In-memory document storage
_generated_documents: dict[str, dict[str, bytes]] = {}


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

    # Store the generated document
    if project_id not in _generated_documents:
        _generated_documents[project_id] = {}
    _generated_documents[project_id][chapter] = doc_bytes

    return {
        "message": f"Document generated successfully for chapter: {chapter}",
        "chapter": chapter,
        "size_bytes": len(doc_bytes),
    }


@router.get("/{project_id}/download/{chapter}")
async def download_document(project_id: str, chapter: str):
    """Download a generated document."""
    if project_id not in _generated_documents:
        raise HTTPException(status_code=404, detail="No documents generated for this project")

    if chapter not in _generated_documents[project_id]:
        raise HTTPException(
            status_code=404, detail=f"Document not found for chapter: {chapter}"
        )

    doc_bytes = _generated_documents[project_id][chapter]
    filename = f"{chapter}.docx"

    return Response(
        content=doc_bytes,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


@router.get("/{project_id}/list")
async def list_documents(project_id: str):
    """List all generated documents for a project."""
    if project_id not in _generated_documents:
        return {"documents": []}

    documents = [
        {"chapter": chapter, "size_bytes": len(doc_bytes)}
        for chapter, doc_bytes in _generated_documents[project_id].items()
    ]
    return {"documents": documents}
