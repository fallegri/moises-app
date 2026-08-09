"""Knowledge base service for indexing and searching markdown files."""

import os
import re
from pathlib import Path
from typing import Optional

from app.core.config import settings


class KnowledgeDocument:
    """Represents a loaded knowledge document."""

    def __init__(self, filename: str, content: str, path: str):
        self.filename = filename
        self.content = content
        self.path = path
        self.sections = self._parse_sections(content)

    def _parse_sections(self, content: str) -> list[dict[str, str]]:
        """Parse content into sections based on markdown headings."""
        sections = []
        current_heading = "Introduction"
        current_content = []

        for line in content.split("\n"):
            if line.startswith("#"):
                if current_content:
                    sections.append(
                        {
                            "heading": current_heading,
                            "content": "\n".join(current_content).strip(),
                        }
                    )
                current_heading = line.lstrip("#").strip()
                current_content = []
            else:
                current_content.append(line)

        if current_content:
            sections.append(
                {
                    "heading": current_heading,
                    "content": "\n".join(current_content).strip(),
                }
            )

        return sections


class KnowledgeBaseService:
    """Service for indexing and searching the knowledge base."""

    def __init__(self, base_path: Optional[str] = None):
        self.base_path = base_path or settings.knowledge_base_path
        self.documents: list[KnowledgeDocument] = []
        self._load_documents()

    def _load_documents(self):
        """Load all markdown files from the knowledge base directory."""
        kb_path = Path(self.base_path)
        if not kb_path.is_absolute():
            # Resolve relative to the backend directory
            kb_path = Path(__file__).parent.parent.parent / self.base_path

        if not kb_path.exists():
            return

        for md_file in sorted(kb_path.glob("*.md")):
            try:
                content = md_file.read_text(encoding="utf-8")
                doc = KnowledgeDocument(
                    filename=md_file.name,
                    content=content,
                    path=str(md_file),
                )
                self.documents.append(doc)
            except Exception:
                # Skip files that cannot be read
                continue

    def search(self, query: str, max_results: int = 5) -> list[dict]:
        """Search the knowledge base for relevant content."""
        results = []
        query_terms = [term.lower() for term in query.split() if len(term) > 2]

        if not query_terms:
            return results

        for doc in self.documents:
            for section in doc.sections:
                score = 0
                section_text = (
                    section["heading"].lower() + " " + section["content"].lower()
                )
                for term in query_terms:
                    count = section_text.count(term)
                    if count > 0:
                        score += count

                if score > 0:
                    results.append(
                        {
                            "filename": doc.filename,
                            "heading": section["heading"],
                            "content": section["content"][:500],
                            "score": score,
                        }
                    )

        # Sort by score descending
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:max_results]

    def get_context_for_phase(self, phase: str, max_chars: int = 3000) -> str:
        """Build a context string from relevant knowledge base content for a given phase."""
        phase_keywords = {
            "problem_identification": "problema investigacion identificar situacion problematica",
            "instrument_suggestion": "instrumentos recopilacion encuesta entrevista observacion",
            "problem_refinement": "formulacion problema metodo cientifico planteamiento",
            "research_question": "pregunta investigacion formulacion objetivos",
            "introduction": "introduccion capitulo redaccion academica",
            "state_of_art": "antecedentes estado cuestion marco teorico",
            "problem_identification_chapter": "planteamiento problema capitulo",
            "specific_problems": "problemas especificos derivados",
            "research_objective": "objetivo general investigacion",
            "specific_objectives": "objetivos especificos",
            "methodological_framework": "marco metodologico variables operacionalizacion",
            "data_collection_instruments": "instrumentos recoleccion datos validacion",
        }

        keywords = phase_keywords.get(phase, phase)
        results = self.search(keywords, max_results=3)

        context_parts = []
        current_chars = 0

        for result in results:
            content = f"[{result['filename']}] {result['heading']}:\n{result['content']}"
            if current_chars + len(content) > max_chars:
                break
            context_parts.append(content)
            current_chars += len(content)

        return "\n\n---\n\n".join(context_parts)

    def get_all_filenames(self) -> list[str]:
        """Get all loaded document filenames."""
        return [doc.filename for doc in self.documents]
