"""SQLAlchemy ORM models for PostgreSQL persistence."""

from sqlalchemy import Column, String, Boolean, DateTime, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime


class Base(DeclarativeBase):
    """Base class for all ORM models."""
    pass


class ResearchProjectDB(Base):
    """SQLAlchemy model for research projects."""
    __tablename__ = "research_projects"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    status = Column(String, nullable=False, default="active")
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    # Complex nested fields stored as JSONB
    problem_description = Column(JSONB, nullable=True)
    suggested_instruments = Column(JSONB, nullable=False, default=list)
    refined_problems = Column(JSONB, nullable=False, default=list)
    selected_problem = Column(JSONB, nullable=True)
    research_question = Column(JSONB, nullable=True)
    introduction = Column(JSONB, nullable=True)
    state_of_art = Column(JSONB, nullable=False, default=dict)
    specific_problems = Column(JSONB, nullable=False, default=list)
    research_objective = Column(JSONB, nullable=True)
    specific_objectives = Column(JSONB, nullable=False, default=list)
    methodological_framework = Column(JSONB, nullable=False, default=dict)
    additional_literature = Column(JSONB, nullable=False, default=list)


class WorkflowStateDB(Base):
    """SQLAlchemy model for workflow states."""
    __tablename__ = "workflow_states"

    project_id = Column(String, primary_key=True)
    current_phase = Column(String, nullable=False, default="problem_identification")
    completed_phases = Column(JSONB, nullable=False, default=list)
    current_tasks = Column(JSONB, nullable=False, default=list)
    phase_data = Column(JSONB, nullable=False, default=dict)
    coherence_validated = Column(Boolean, nullable=False, default=False)
    last_validation_message = Column(Text, nullable=True)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)


class AIConfigDB(Base):
    """SQLAlchemy model for AI configuration."""
    __tablename__ = "ai_config"

    id = Column(String, primary_key=True, default="default")
    config_data = Column(JSONB, nullable=False, default=dict)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
