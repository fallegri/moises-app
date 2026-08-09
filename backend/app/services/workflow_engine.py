"""Workflow engine managing the step-by-step research process."""

from typing import Optional, Any

from app.models.workflow import WorkflowPhase, WorkflowState, PhaseTask, PHASE_ORDER
from app.models.research_project import (
    ResearchProject,
    ProblemDescription,
    RefinedProblem,
    ResearchQuestion,
    SimilarStudy,
    StateOfArtMatrix,
    SpecificProblem,
    ResearchObjective,
    SpecificObjective,
    MethodologicalFramework,
)
from app.services.ai_service import AIService
from app.services.knowledge_base import KnowledgeBaseService


class WorkflowEngine:
    """Manages the step-by-step research workflow process."""

    def __init__(
        self,
        ai_service: Optional[AIService] = None,
        knowledge_base: Optional[KnowledgeBaseService] = None,
    ):
        self.ai_service = ai_service or AIService()
        self.knowledge_base = knowledge_base or KnowledgeBaseService()

    def initialize_workflow(self, project_id: str) -> WorkflowState:
        """Initialize a new workflow state for a project."""
        state = WorkflowState(project_id=project_id)
        state.current_tasks = self._get_phase_tasks(state.current_phase)
        return state

    def get_phase_description(self, phase: WorkflowPhase) -> dict[str, str]:
        """Get human-readable description and instructions for a phase."""
        descriptions = {
            WorkflowPhase.PROBLEM_IDENTIFICATION: {
                "title": "Identificacion del Problema",
                "description": (
                    "Describa la situacion problematica que ha observado. "
                    "Incluya antecedentes, datos y contexto relevante."
                ),
                "instruction": (
                    "El sistema analizara su descripcion para identificar "
                    "el problema aparente en la situacion descrita."
                ),
            },
            WorkflowPhase.INSTRUMENT_SUGGESTION: {
                "title": "Sugerencia de Instrumentos",
                "description": (
                    "El sistema sugiere instrumentos para recopilar mas "
                    "informacion que ayude a identificar mejor el problema."
                ),
                "instruction": (
                    "Utilice los instrumentos sugeridos para recopilar datos. "
                    "Puede subir los resultados en formato Word, Excel o Markdown."
                ),
            },
            WorkflowPhase.PROBLEM_REFINEMENT: {
                "title": "Refinamiento del Problema",
                "description": (
                    "Con los datos recopilados, el sistema refinara el problema "
                    "y ofrecera 3 formulaciones usando el metodo cientifico."
                ),
                "instruction": "Seleccione la formulacion que mejor represente su problema de investigacion.",
            },
            WorkflowPhase.RESEARCH_QUESTION: {
                "title": "Pregunta de Investigacion",
                "description": (
                    "A partir del problema seleccionado, se formulara "
                    "la pregunta de investigacion principal."
                ),
                "instruction": "Revise y valide la pregunta de investigacion propuesta.",
            },
            WorkflowPhase.INTRODUCTION: {
                "title": "Capitulo: Introduccion",
                "description": "Se generara el capitulo de introduccion de la investigacion.",
                "instruction": "Revise el contenido generado y proporcione ajustes si es necesario.",
            },
            WorkflowPhase.STATE_OF_ART: {
                "title": "Antecedentes / Estado de la Cuestion",
                "description": (
                    "Proporcione al menos 6 investigaciones similares. "
                    "Se construira una matriz de estado de la cuestion."
                ),
                "instruction": (
                    "Ingrese los datos de cada investigacion similar. "
                    "Si no encuentra 6, marque 'no mas investigaciones encontradas'."
                ),
            },
            WorkflowPhase.PROBLEM_IDENTIFICATION_CHAPTER: {
                "title": "Capitulo: Identificacion del Problema",
                "description": "Se generara el capitulo de planteamiento del problema.",
                "instruction": "Revise y valide el capitulo generado.",
            },
            WorkflowPhase.SPECIFIC_PROBLEMS: {
                "title": "Problemas Especificos",
                "description": "Se derivaran los problemas especificos del problema principal.",
                "instruction": "Revise los problemas especificos propuestos.",
            },
            WorkflowPhase.RESEARCH_OBJECTIVE: {
                "title": "Objetivo de Investigacion",
                "description": "Se formulara el objetivo general de la investigacion.",
                "instruction": "Valide que el objetivo sea coherente con la pregunta de investigacion.",
            },
            WorkflowPhase.SPECIFIC_OBJECTIVES: {
                "title": "Objetivos Especificos",
                "description": "Se formularan los objetivos especificos alineados a los problemas especificos.",
                "instruction": "Verifique la coherencia entre objetivos especificos y problemas especificos.",
            },
            WorkflowPhase.METHODOLOGICAL_FRAMEWORK: {
                "title": "Marco Metodologico",
                "description": (
                    "Se definira el marco metodologico incluyendo la "
                    "matriz de conceptualizacion de variables."
                ),
                "instruction": "Revise la operacionalizacion de variables propuesta.",
            },
            WorkflowPhase.DATA_COLLECTION_INSTRUMENTS: {
                "title": "Instrumentos de Recoleccion de Datos",
                "description": "Se diseñaran los instrumentos para recopilar informacion.",
                "instruction": "Revise los instrumentos propuestos para la recoleccion de datos.",
            },
        }
        return descriptions.get(
            phase,
            {
                "title": phase.value,
                "description": "",
                "instruction": "",
            },
        )

    def _get_phase_tasks(self, phase: WorkflowPhase) -> list[PhaseTask]:
        """Get the tasks for a given phase."""
        phase_tasks = {
            WorkflowPhase.PROBLEM_IDENTIFICATION: [
                PhaseTask(
                    description="Describir la situacion problematica",
                    instruction=(
                        "Redacte una descripcion detallada de la situacion "
                        "problematica que ha observado, incluyendo antecedentes y datos."
                    ),
                )
            ],
            WorkflowPhase.INSTRUMENT_SUGGESTION: [
                PhaseTask(
                    description="Revisar instrumentos sugeridos",
                    instruction="Revise los instrumentos sugeridos por el sistema para recopilar datos.",
                ),
                PhaseTask(
                    description="Subir datos recopilados",
                    instruction=(
                        "Suba los datos recopilados usando los instrumentos "
                        "(archivos .docx, .xlsx o .md)."
                    ),
                ),
            ],
            WorkflowPhase.PROBLEM_REFINEMENT: [
                PhaseTask(
                    description="Seleccionar formulacion del problema",
                    instruction=(
                        "El sistema presentara 3 formulaciones del problema. "
                        "Seleccione la que mejor represente su investigacion."
                    ),
                )
            ],
            WorkflowPhase.RESEARCH_QUESTION: [
                PhaseTask(
                    description="Validar pregunta de investigacion",
                    instruction="Revise y apruebe la pregunta de investigacion propuesta.",
                )
            ],
            WorkflowPhase.INTRODUCTION: [
                PhaseTask(
                    description="Revisar capitulo de introduccion",
                    instruction="Revise el capitulo de introduccion generado.",
                )
            ],
            WorkflowPhase.STATE_OF_ART: [
                PhaseTask(
                    description="Agregar investigaciones similares",
                    instruction=(
                        "Ingrese al menos 6 investigaciones similares. "
                        "Si no encuentra mas, active la casilla correspondiente."
                    ),
                )
            ],
            WorkflowPhase.PROBLEM_IDENTIFICATION_CHAPTER: [
                PhaseTask(
                    description="Revisar capitulo de planteamiento del problema",
                    instruction="Revise el capitulo de planteamiento del problema generado.",
                )
            ],
            WorkflowPhase.SPECIFIC_PROBLEMS: [
                PhaseTask(
                    description="Validar problemas especificos",
                    instruction="Revise y valide los problemas especificos derivados.",
                )
            ],
            WorkflowPhase.RESEARCH_OBJECTIVE: [
                PhaseTask(
                    description="Validar objetivo de investigacion",
                    instruction="Revise el objetivo general propuesto.",
                )
            ],
            WorkflowPhase.SPECIFIC_OBJECTIVES: [
                PhaseTask(
                    description="Validar objetivos especificos",
                    instruction="Revise los objetivos especificos propuestos.",
                )
            ],
            WorkflowPhase.METHODOLOGICAL_FRAMEWORK: [
                PhaseTask(
                    description="Revisar marco metodologico",
                    instruction=(
                        "Revise el marco metodologico y la matriz "
                        "de conceptualizacion de variables."
                    ),
                )
            ],
            WorkflowPhase.DATA_COLLECTION_INSTRUMENTS: [
                PhaseTask(
                    description="Revisar instrumentos de recoleccion",
                    instruction="Revise los instrumentos de recoleccion de datos propuestos.",
                )
            ],
        }
        return phase_tasks.get(phase, [])

    def process_input(
        self,
        state: WorkflowState,
        project: ResearchProject,
        user_input: str,
    ) -> dict[str, Any]:
        """Process user input for the current phase.

        Returns a dict with 'result' (AI response) and updated state/project.
        """
        phase = state.current_phase
        knowledge_context = self.knowledge_base.get_context_for_phase(phase.value)

        result = {}

        if phase == WorkflowPhase.PROBLEM_IDENTIFICATION:
            ai_response = self.ai_service.analyze_problem(user_input, knowledge_context)
            project.problem_description = ProblemDescription(
                raw_text=user_input,
                identified_problem=ai_response,
            )
            result = {"identified_problem": ai_response}

        elif phase == WorkflowPhase.INSTRUMENT_SUGGESTION:
            problem = (
                project.problem_description.identified_problem
                if project.problem_description
                else user_input
            )
            ai_response = self.ai_service.suggest_instruments(
                problem or user_input, knowledge_context
            )
            result = {"suggested_instruments": ai_response, "uploaded_data": user_input}

        elif phase == WorkflowPhase.PROBLEM_REFINEMENT:
            problem = (
                project.problem_description.identified_problem
                if project.problem_description
                else ""
            )
            ai_response = self.ai_service.refine_problem(
                problem or "", user_input, knowledge_context
            )
            result = {"refined_formulations": ai_response}

        elif phase == WorkflowPhase.RESEARCH_QUESTION:
            selected = (
                project.selected_problem.formulation
                if project.selected_problem
                else user_input
            )
            ai_response = self.ai_service.generate_research_questions(
                selected, knowledge_context
            )
            result = {"research_questions": ai_response}

        elif phase == WorkflowPhase.STATE_OF_ART:
            # Handle state-of-art phase: user submits study data
            # Parse the input as a study entry and add to the project's state_of_art
            project_context = self._build_project_context(project)
            ai_response = self.ai_service.generate_chapter(
                phase.value, user_input, project_context, knowledge_context
            )
            result = {
                "generated_content": ai_response,
                "studies_count": len(project.state_of_art.studies),
                "no_more_studies_found": project.state_of_art.no_more_studies_found,
                "can_proceed": (
                    len(project.state_of_art.studies) >= 6
                    or project.state_of_art.no_more_studies_found
                ),
            }

        else:
            # For chapter generation phases
            project_context = self._build_project_context(project)
            ai_response = self.ai_service.generate_chapter(
                phase.value, user_input, project_context, knowledge_context
            )
            result = {"generated_content": ai_response}

        state.phase_data[phase.value] = result
        return result

    def validate_phase_coherence(
        self,
        state: WorkflowState,
        project: ResearchProject,
    ) -> dict[str, Any]:
        """Validate coherence for the current phase before advancing."""
        phase = state.current_phase
        knowledge_context = self.knowledge_base.get_context_for_phase(phase.value)

        current_data = str(state.phase_data.get(phase.value, ""))
        previous_data = self._build_project_context(project)

        validation_result = self.ai_service.validate_coherence(
            phase.value, current_data, previous_data, knowledge_context
        )

        # Parse validation - we expect the AI to indicate coherence
        is_coherent = self._parse_coherence_result(validation_result)
        state.coherence_validated = is_coherent
        state.last_validation_message = validation_result

        return {
            "is_coherent": is_coherent,
            "message": validation_result,
        }

    def _parse_coherence_result(self, result: str) -> bool:
        """Parse AI coherence validation response."""
        result_lower = result.lower()
        positive_indicators = ["coherente", "coherent", "valido", "valid", "aprobado", "approved"]
        negative_indicators = ["incoherente", "incoherent", "invalido", "invalid", "rechazado"]

        for indicator in negative_indicators:
            if indicator in result_lower:
                return False

        for indicator in positive_indicators:
            if indicator in result_lower:
                return True

        # Default to false if no clear indicator (fail-closed)
        return False

    def advance_phase(self, state: WorkflowState) -> Optional[WorkflowPhase]:
        """Advance to the next phase."""
        new_phase = state.advance_phase()
        if new_phase:
            state.current_tasks = self._get_phase_tasks(new_phase)
        return new_phase

    def add_similar_study(
        self,
        project: ResearchProject,
        study: SimilarStudy,
    ) -> dict[str, Any]:
        """Add a similar study to the state-of-art matrix."""
        project.state_of_art.studies.append(study)
        return {
            "studies_count": len(project.state_of_art.studies),
            "can_proceed": (
                len(project.state_of_art.studies) >= 6
                or project.state_of_art.no_more_studies_found
            ),
        }

    def set_no_more_studies(
        self,
        project: ResearchProject,
        state: WorkflowState,
        no_more: bool,
    ) -> dict[str, Any]:
        """Set the 'no more studies found' flag for the state-of-art phase.

        When checked, allows advancing with fewer than 6 studies.
        """
        project.state_of_art.no_more_studies_found = no_more
        studies_count = len(project.state_of_art.studies)
        can_proceed = studies_count >= 6 or no_more
        return {
            "no_more_studies_found": no_more,
            "studies_count": studies_count,
            "can_proceed": can_proceed,
        }

    def can_advance_state_of_art(self, project: ResearchProject) -> bool:
        """Check if the state-of-art phase can advance.

        Requires at least 6 studies, or fewer if 'no_more_studies_found' is checked.
        """
        studies_count = len(project.state_of_art.studies)
        return studies_count >= 6 or (
            project.state_of_art.no_more_studies_found and studies_count > 0
        )

    def _build_project_context(self, project: ResearchProject) -> str:
        """Build a context string from all project data accumulated so far."""
        parts = []

        if project.problem_description:
            parts.append(f"Situacion problematica: {project.problem_description.raw_text}")
            if project.problem_description.identified_problem:
                parts.append(
                    f"Problema identificado: {project.problem_description.identified_problem}"
                )

        if project.selected_problem:
            parts.append(f"Problema seleccionado: {project.selected_problem.formulation}")

        if project.research_question:
            parts.append(
                f"Pregunta de investigacion: {project.research_question.main_question}"
            )

        if project.specific_problems:
            problems = [sp.statement for sp in project.specific_problems]
            parts.append(f"Problemas especificos: {'; '.join(problems)}")

        if project.research_objective:
            parts.append(f"Objetivo general: {project.research_objective.statement}")

        if project.specific_objectives:
            objectives = [so.statement for so in project.specific_objectives]
            parts.append(f"Objetivos especificos: {'; '.join(objectives)}")

        return "\n\n".join(parts)
