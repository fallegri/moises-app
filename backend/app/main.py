"""FastAPI application entry point."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers import projects, workflow, documents, knowledge, ai_config


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan: initialize database tables on startup if configured."""
    if settings.database_url:
        from app.db.init_db import create_tables
        create_tables()
    yield


app = FastAPI(
    title=settings.app_name,
    description="AI-powered research assistant that guides users through the scientific research process",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS middleware - uses effective_cors_origins which includes FRONTEND_URL if set
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.effective_cors_origins,
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
