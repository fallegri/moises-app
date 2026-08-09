"""Knowledge base search and literature upload endpoints."""

from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel

from app.services.knowledge_base import KnowledgeBaseService
from app.services.file_parser import FileParserService

router = APIRouter()

# Service instances
_knowledge_base = KnowledgeBaseService()
_file_parser = FileParserService()


class SearchResponse(BaseModel):
    """Response model for knowledge base search."""
    results: list[dict]
    query: str
    total_results: int


@router.get("/search")
async def search_knowledge_base(q: str, max_results: int = 5):
    """Search the knowledge base for relevant content."""
    if not q.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    results = _knowledge_base.search(q, max_results=max_results)
    return {
        "query": q,
        "results": results,
        "total_results": len(results),
    }


@router.get("/documents")
async def list_knowledge_documents():
    """List all documents in the knowledge base."""
    filenames = _knowledge_base.get_all_filenames()
    return {
        "documents": filenames,
        "total": len(filenames),
    }


@router.post("/upload")
async def upload_literature(file: UploadFile = File(...)):
    """Upload additional literature files to the knowledge base."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is required")

    # Validate file type
    allowed_extensions = {".docx", ".xlsx", ".md", ".txt"}
    extension = "." + file.filename.rsplit(".", 1)[-1].lower() if "." in file.filename else ""
    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {extension}. Allowed: {', '.join(allowed_extensions)}",
        )

    try:
        content = await file.read()
        extracted_text = _file_parser.parse_file(content, file.filename)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

    # Add the extracted text to the knowledge base so it becomes searchable
    from app.services.knowledge_base import KnowledgeDocument as KBDocument
    new_doc = KBDocument(
        filename=file.filename,
        content=extracted_text,
        path=f"uploaded/{file.filename}",
    )
    _knowledge_base.documents.append(new_doc)

    return {
        "filename": file.filename,
        "extracted_text_length": len(extracted_text),
        "preview": extracted_text[:500],
        "message": "File uploaded and processed successfully",
    }
