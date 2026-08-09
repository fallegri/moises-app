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
    content: Optional[str] = None
    author: Optional[str] = None
    references: Optional[list[str]] = None


def _derive_content_from_project(project, chapter: str) -> str:
    """Derive document content from the project's persisted phase data."""
    sections = []

    if chapter == "introduction" and project.introduction:
        sections.append(project.introduction.content)
    elif chapter == "problem_identification" and project.problem_description:
        if project.problem_description.raw_text:
            sections.append(project.problem_description.raw_text)
        if project.problem_description.identified_problem:
            sections.append(f"\nProblema identificado: {project.problem_description.identified_problem}")
    elif chapter == "problem_refinement" and project.selected_problem:
        sections.append(f"Formulacion del problema: {project.selected_problem.formulation}")
        sections.append(f"Base metodologica: {project.selected_problem.methodology_basis}")
    elif chapter == "research_question" and project.research_question:
        sections.append(f"Pregunta principal: {project.research_question.main_question}")
        sections.append(f"Justificacion: {project.research_question.justification}")
        if project.research_question.scope:
            sections.append(f"Alcance: {project.research_question.scope}")
    elif chapter == "state_of_art" and project.state_of_art.studies:
        sections.append("Estado de la cuestion:\n")
        for study in project.state_of_art.studies:
            sections.append(
                f"- {study.title} ({study.authors}, {study.year}): "
                f"{study.findings}. Relevancia: {study.relevance}"
            )
        if project.state_of_art.synthesis:
            sections.append(f"\nSintesis: {project.state_of_art.synthesis}")
    elif chapter == "specific_problems" and project.specific_problems:
        for i, sp in enumerate(project.specific_problems, 1):
            sections.append(f"{i}. {sp.statement}")
            sections.append(f"   Relacion con problema principal: {sp.relationship_to_main}")
    elif chapter == "research_objective" and project.research_objective:
        sections.append(f"Objetivo general: {project.research_objective.statement}")
        sections.append(f"Alineacion: {project.research_objective.alignment_with_question}")
    elif chapter == "specific_objectives" and project.specific_objectives:
        for i, obj in enumerate(project.specific_objectives, 1):
            sections.append(f"{i}. {obj.statement}")
            if obj.measurable_indicator:
                sections.append(f"   Indicador: {obj.measurable_indicator}")
    elif chapter == "methodological_framework":
        mf = project.methodological_framework
        if mf.research_type:
            sections.append(f"Tipo de investigacion: {mf.research_type}")
        if mf.research_design:
            sections.append(f"Diseno: {mf.research_design}")
        if mf.population:
            sections.append(f"Poblacion: {mf.population}")
        if mf.sample:
            sections.append(f"Muestra: {mf.sample}")
        if mf.variable_matrix.variables:
            sections.append("\nMatriz de variables:")
            for v in mf.variable_matrix.variables:
                sections.append(
                    f"- {v.name} ({v.type}): {v.conceptual_definition}"
                )
    elif chapter == "data_collection_instruments":
        for inst in project.methodological_framework.instruments:
            sections.append(f"Instrumento: {inst.name} ({inst.type})")
            sections.append(f"Variable objetivo: {inst.target_variable}")
            if inst.items:
                sections.append(f"Items: {', '.join(inst.items)}")

    if not sections:
        # Fallback: return a placeholder indicating no data is available yet
        return f"Contenido del capitulo: {chapter.replace('_', ' ').title()}\n\n(Sin datos disponibles para este capitulo.)"

    return "\n".join(sections)


@router.post("/{project_id}/generate/{chapter}")
async def generate_document(
    project_id: str, chapter: str, request: Optional[GenerateDocumentRequest] = None
):
    """Generate an APA 7 formatted document for a chapter."""
    if project_id not in _projects:
        raise HTTPException(status_code=404, detail="Project not found")

    project = _projects[project_id]
    title = f"{chapter.replace('_', ' ').title()} - {project.title or 'Investigacion'}"

    # If no request body or no content provided, derive from project data
    content = None
    author = None
    references = None
    if request:
        content = request.content
        author = request.author
        references = request.references

    if not content:
        content = _derive_content_from_project(project, chapter)

    try:
        doc_bytes = _generator.create_document(
            title=title,
            content=content,
            author=author,
            references=references,
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
