"""Pydantic models for research project entities."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum
import uuid


class ProjectStatus(str, Enum):
    """Status of a research project."""
    ACTIVE = "active"
    COMPLETED = "completed"
    ARCHIVED = "archived"


class ProblemDescription(BaseModel):
    """Initial problem description submitted by the user."""
    raw_text: str = Field(..., description="User's description of the problematic situation")
    identified_problem: Optional[str] = Field(None, description="AI-identified apparent problem")
    context_notes: Optional[str] = None


class SuggestedInstrument(BaseModel):
    """An instrument suggested to better identify the problem."""
    name: str
    description: str
    purpose: str
    template: Optional[str] = None


class RefinedProblem(BaseModel):
    """Refined problem formulation using the scientific method."""
    formulation: str = Field(..., description="Problem statement formulation")
    methodology_basis: str = Field(..., description="Scientific method basis for this formulation")
    selected: bool = False


class ResearchQuestion(BaseModel):
    """Research question derived from the problem."""
    main_question: str
    justification: str
    scope: Optional[str] = None


class SpecificProblem(BaseModel):
    """Specific problem derived from the main problem."""
    statement: str
    relationship_to_main: str


class ResearchObjective(BaseModel):
    """Main research objective."""
    statement: str
    alignment_with_question: str


class SpecificObjective(BaseModel):
    """Specific research objective."""
    statement: str
    alignment_with_specific_problem: str
    measurable_indicator: Optional[str] = None


class SimilarStudy(BaseModel):
    """A similar study for the state of the art."""
    title: str
    authors: str
    year: int
    methodology: str
    findings: str
    relevance: str
    source: Optional[str] = None


class StateOfArtMatrix(BaseModel):
    """Matrix of state of the art / background studies."""
    studies: list[SimilarStudy] = Field(default_factory=list)
    no_more_studies_found: bool = False
    synthesis: Optional[str] = None


class Variable(BaseModel):
    """Research variable for the conceptualization matrix."""
    name: str
    type: str = Field(..., description="Independent, dependent, or intervening")
    conceptual_definition: str
    operational_definition: str
    dimensions: list[str] = Field(default_factory=list)
    indicators: list[str] = Field(default_factory=list)


class VariableConceptualizationMatrix(BaseModel):
    """Matrix for variable conceptualization in methodological framework."""
    variables: list[Variable] = Field(default_factory=list)


class DataCollectionInstrument(BaseModel):
    """Data collection instrument details."""
    name: str
    type: str = Field(..., description="Survey, interview, observation, etc.")
    target_variable: str
    items: list[str] = Field(default_factory=list)
    validation_method: Optional[str] = None


class MethodologicalFramework(BaseModel):
    """Methodological framework for the research."""
    research_type: Optional[str] = None
    research_design: Optional[str] = None
    population: Optional[str] = None
    sample: Optional[str] = None
    sampling_method: Optional[str] = None
    variable_matrix: VariableConceptualizationMatrix = Field(
        default_factory=VariableConceptualizationMatrix
    )
    instruments: list[DataCollectionInstrument] = Field(default_factory=list)


class IntroductionChapter(BaseModel):
    """Introduction chapter content."""
    content: str
    generated_at: Optional[datetime] = None


class ResearchProject(BaseModel):
    """Complete research project model."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: Optional[str] = None
    status: ProjectStatus = ProjectStatus.ACTIVE
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Phase data
    problem_description: Optional[ProblemDescription] = None
    suggested_instruments: list[SuggestedInstrument] = Field(default_factory=list)
    refined_problems: list[RefinedProblem] = Field(default_factory=list)
    selected_problem: Optional[RefinedProblem] = None
    research_question: Optional[ResearchQuestion] = None
    introduction: Optional[IntroductionChapter] = None
    state_of_art: StateOfArtMatrix = Field(default_factory=StateOfArtMatrix)
    specific_problems: list[SpecificProblem] = Field(default_factory=list)
    research_objective: Optional[ResearchObjective] = None
    specific_objectives: list[SpecificObjective] = Field(default_factory=list)
    methodological_framework: MethodologicalFramework = Field(
        default_factory=MethodologicalFramework
    )

    # Additional literature uploaded by user
    additional_literature: list[str] = Field(
        default_factory=list, description="Paths to additional literature files uploaded"
    )
