"""Database initialization - creates all tables."""

from app.db.models import Base
from app.db.session import get_engine


def create_tables():
    """Create all database tables if they don't exist."""
    engine = get_engine()
    if engine is not None:
        Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully.")
