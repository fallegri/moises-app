"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers import projects, workflow, documents, knowledge

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

# Include routers
app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(workflow.router, prefix="/workflow", tags=["workflow"])
app.include_router(documents.router, prefix="/documents", tags=["documents"])
app.include_router(knowledge.router, prefix="/knowledge", tags=["knowledge"])


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": settings.app_name}
