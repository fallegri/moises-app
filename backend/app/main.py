"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers import projects, workflow, documents, knowledge, ai_config

app = FastAPI(
    title=settings.app_name,
    description="AI-powered research assistant that guides users through the scientific research process",
    version="1.0.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with /api prefix to match frontend expectations
app.include_router(projects.router, prefix="/api/projects", tags=["projects"])
app.include_router(workflow.router, prefix="/api/workflow", tags=["workflow"])
app.include_router(documents.router, prefix="/api/documents", tags=["documents"])
app.include_router(knowledge.router, prefix="/api/knowledge", tags=["knowledge"])
app.include_router(ai_config.router, prefix="/api/ai-config", tags=["ai-config"])


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": settings.app_name}
