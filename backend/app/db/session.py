"""Database session configuration for synchronous SQLAlchemy."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.core.config import settings

# Engine and session factory - only created when DATABASE_URL is configured
_engine = None
_SessionLocal = None


def get_engine():
    """Get or create the SQLAlchemy engine."""
    global _engine
    if _engine is None and settings.database_url:
        # Convert asyncpg URL to psycopg2 if needed
        url = settings.database_url
        if url.startswith("postgresql+asyncpg://"):
            url = url.replace("postgresql+asyncpg://", "postgresql://")
        elif url.startswith("postgres://"):
            url = url.replace("postgres://", "postgresql://", 1)
        _engine = create_engine(url, pool_pre_ping=True)
    return _engine


def get_session() -> Session:
    """Get a new database session."""
    global _SessionLocal
    if _SessionLocal is None:
        engine = get_engine()
        if engine is None:
            raise RuntimeError("Database not configured. Set DATABASE_URL environment variable.")
        _SessionLocal = sessionmaker(bind=engine)
    return _SessionLocal()
