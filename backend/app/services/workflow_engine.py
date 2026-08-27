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
from app.services.ai_service import AIService, AIServiceConfigError
from app.services.knowledge_base import KnowledgeBaseService


# Advisory message shown when a phase is submitted but no AI is configured, so
# the flow keeps working (input is persisted) instead of hard-failing with a 500.
AI_UNCONFIGURED_MESSAGE = (
    "La IA no esta configurada, por lo que no se genero una respuesta "
    "automatica. Su texto se guardo correctamente. Configure la IA en el panel "
    "de ajustes para obtener el analisis, o continue a la siguiente fase."
)


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
        # Nota consistente sobre el archivo opcional, reutilizada en las fases
        # que aceptan material de respaldo.
        optional_upload = (
            "Opcional: puede adjuntar documentos de respaldo (.docx, .xlsx, .md)."
        )

        descriptions = {
            WorkflowPhase.PROBLEM_IDENTIFICATION: {
                "title": "Identificacion del Problema",
                "description": (
                    "En esta fase usted describe con sus propias palabras la "
                    "situacion problematica que ha observado. El objetivo es que "
                    "la IA identifique el problema aparente a partir de su relato."
                ),
                "instruction": (
                    "Escriba en el cuadro de texto una descripcion de la situacion "
                    "problematica: antecedentes, datos concretos (cifras, fechas, "
                    "personas afectadas) y el contexto en que ocurre. No necesita "
                    "subir ningun archivo para continuar. " + optional_upload
                ),
            },
            WorkflowPhase.INSTRUMENT_SUGGESTION: {
                "title": "Sugerencia de Instrumentos",
                "description": (
                    "La IA propone instrumentos (encuestas, entrevistas, "
                    "observaciones) para recopilar mas informacion y precisar el "
                    "problema. Usted aplica esos instrumentos y reporta lo obtenido."
                ),
                "instruction": (
                    "Escriba en el cuadro de texto un resumen de los datos que "
                    "recopilo al aplicar los instrumentos sugeridos. " + optional_upload
                    + " Los archivos ayudan a la IA a analizar mejor sus datos."
                ),
            },
            WorkflowPhase.PROBLEM_REFINEMENT: {
                "title": "Refinamiento del Problema",
                "description": (
                    "Con los datos recopilados, la IA refina el problema y ofrece "
                    "3 formulaciones alternativas construidas con el metodo "
                    "cientifico para que usted elija la mas adecuada."
                ),
                "instruction": (
                    "Escriba en el cuadro de texto los datos o hallazgos que la IA "
                    "debe considerar para reformular el problema. Luego seleccione "
                    "la formulacion que mejor represente su investigacion. "
                    + optional_upload
                ),
            },
            WorkflowPhase.RESEARCH_QUESTION: {
                "title": "Pregunta de Investigacion",
                "description": (
                    "A partir del problema seleccionado, la IA formula la pregunta "
                    "de investigacion principal que guiara todo el estudio."
                ),
                "instruction": (
                    "Escriba en el cuadro de texto cualquier aclaracion o enfoque "
                    "que desee para la pregunta, luego revise y valide la pregunta "
                    "de investigacion propuesta. " + optional_upload
                ),
            },
            WorkflowPhase.INTRODUCTION: {
                "title": "Capitulo: Introduccion",
                "description": (
                    "La IA genera el capitulo de introduccion de la investigacion "
                    "a partir de la informacion acumulada en las fases anteriores."
                ),
                "instruction": (
                    "Escriba en el cuadro de texto los ajustes o enfasis que desea "
                    "para la introduccion y revise el contenido generado. "
                    + optional_upload
                ),
            },
            WorkflowPhase.STATE_OF_ART: {
                "title": "Antecedentes / Estado de la Cuestion",
                "description": (
                    "Registre al menos 6 investigaciones similares a la suya. Con "
                    "ellas se construye la matriz del estado de la cuestion."
                ),
                "instruction": (
                    "Use el formulario para agregar cada investigacion similar "
                    "(titulo, autores, ano, metodologia, hallazgos y relevancia). "
                    "Si no encuentra 6, marque la casilla 'no hay mas "
                    "investigaciones encontradas' para poder continuar. Escriba en "
                    "el cuadro de texto una sintesis del estado de la cuestion. "
                    + optional_upload
                ),
            },
            WorkflowPhase.PROBLEM_IDENTIFICATION_CHAPTER: {
                "title": "Capitulo: Identificacion del Problema",
                "description": (
                    "La IA genera el capitulo de planteamiento del problema "
                    "integrando el problema identificado y los antecedentes."
                ),
                "instruction": (
                    "Escriba en el cuadro de texto los ajustes que desea y revise "
                    "el capitulo generado. " + optional_upload
                ),
            },
            WorkflowPhase.SPECIFIC_PROBLEMS: {
                "title": "Problemas Especificos",
                "description": (
                    "La IA deriva los problemas especificos a partir del problema "
                    "principal para desagregar el objeto de estudio."
                ),
                "instruction": (
                    "Escriba en el cuadro de texto cualquier precision y revise los "
                    "problemas especificos propuestos. " + optional_upload
                ),
            },
            WorkflowPhase.RESEARCH_OBJECTIVE: {
                "title": "Objetivo de Investigacion",
                "description": (
                    "La IA formula el objetivo general de la investigacion, "
                    "alineado con la pregunta de investigacion."
                ),
                "instruction": (
                    "Escriba en el cuadro de texto ajustes al enfoque y valide que "
                    "el objetivo sea coherente con la pregunta de investigacion. "
                    + optional_upload
                ),
            },
            WorkflowPhase.SPECIFIC_OBJECTIVES: {
                "title": "Objetivos Especificos",
                "description": (
                    "La IA formula los objetivos especificos alineados con los "
                    "problemas especificos definidos antes."
                ),
                "instruction": (
                    "Escriba en el cuadro de texto sus observaciones y verifique la "
                    "coherencia entre objetivos especificos y problemas "
                    "especificos. " + optional_upload
                ),
            },
            WorkflowPhase.METHODOLOGICAL_FRAMEWORK: {
                "title": "Marco Metodologico",
                "description": (
                    "Se define el marco metodologico, incluyendo la matriz de "
                    "conceptualizacion y operacionalizacion de variables."
                ),
                "instruction": (
                    "Escriba en el cuadro de texto el enfoque metodologico deseado "
                    "y revise la operacionalizacion de variables propuesta. "
                    + optional_upload
                ),
            },
            WorkflowPhase.DATA_COLLECTION_INSTRUMENTS: {
                "title": "Instrumentos de Recoleccion de Datos",
                "description": (
                    "La IA disena los instrumentos para recopilar la informacion "
                    "necesaria segun el marco metodologico. Esta es la fase final."
                ),
                "instruction": (
                    "Escriba en el cuadro de texto los requisitos de sus "
                    "instrumentos y revise los instrumentos de recoleccion "
                    "propuestos. " + optional_upload
                ),
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
                        "Escriba en el cuadro de texto la situacion problematica que "
                        "observo: antecedentes, datos concretos y contexto. Al enviar, "
                        "la IA identificara el problema. El archivo es opcional."
                    ),
                )
            ],
            WorkflowPhase.INSTRUMENT_SUGGESTION: [
                PhaseTask(
                    description="Reportar los datos recopilados",
                    instruction=(
                        "Revise los instrumentos que sugiere la IA, aplicalos y "
                        "escriba en el cuadro de texto un resumen de los datos que "
                        "obtuvo. Adjuntar los resultados como archivo es opcional."
                    ),
                ),
            ],
            WorkflowPhase.PROBLEM_REFINEMENT: [
                PhaseTask(
                    description="Elegir la formulacion del problema",
                    instruction=(
                        "Escriba los datos o hallazgos que la IA debe considerar y "
                        "envie. La IA propondra 3 formulaciones; seleccione la que "
                        "mejor represente su investigacion. El archivo es opcional."
                    ),
                )
            ],
            WorkflowPhase.RESEARCH_QUESTION: [
                PhaseTask(
                    description="Validar la pregunta de investigacion",
                    instruction=(
                        "Escriba cualquier aclaracion de enfoque y envie para que la "
                        "IA formule la pregunta. Luego revise y apruebe la pregunta "
                        "de investigacion propuesta. El archivo es opcional."
                    ),
                )
            ],
            WorkflowPhase.INTRODUCTION: [
                PhaseTask(
                    description="Revisar el capitulo de introduccion",
                    instruction=(
                        "Escriba los ajustes o enfasis que desea y envie para "
                        "generar el capitulo de introduccion. Luego revise el "
                        "contenido generado. El archivo es opcional."
                    ),
                )
            ],
            WorkflowPhase.STATE_OF_ART: [
                PhaseTask(
                    description="Registrar investigaciones similares",
                    instruction=(
                        "Agregue al menos 6 investigaciones similares con el "
                        "formulario. Si no encuentra 6, marque 'no hay mas "
                        "investigaciones encontradas'. Escriba una sintesis y envie. "
                        "El archivo es opcional."
                    ),
                )
            ],
            WorkflowPhase.PROBLEM_IDENTIFICATION_CHAPTER: [
                PhaseTask(
                    description="Revisar el capitulo de planteamiento del problema",
                    instruction=(
                        "Escriba los ajustes que desea y envie para generar el "
                        "capitulo de planteamiento del problema. Luego revise el "
                        "capitulo generado. El archivo es opcional."
                    ),
                )
            ],
            WorkflowPhase.SPECIFIC_PROBLEMS: [
                PhaseTask(
                    description="Validar los problemas especificos",
                    instruction=(
                        "Escriba cualquier precision y envie para que la IA derive "
                        "los problemas especificos. Luego revise y valide los "
                        "problemas propuestos. El archivo es opcional."
                    ),
                )
            ],
            WorkflowPhase.RESEARCH_OBJECTIVE: [
                PhaseTask(
                    description="Validar el objetivo de investigacion",
                    instruction=(
                        "Escriba ajustes al enfoque y envie para que la IA formule "
                        "el objetivo general. Luego revise el objetivo propuesto. "
                        "El archivo es opcional."
                    ),
                )
            ],
            WorkflowPhase.SPECIFIC_OBJECTIVES: [
                PhaseTask(
                    description="Validar los objetivos especificos",
                    instruction=(
                        "Escriba sus observaciones y envie para que la IA formule "
                        "los objetivos especificos. Luego revise los objetivos "
                        "propuestos. El archivo es opcional."
                    ),
                )
            ],
            WorkflowPhase.METHODOLOGICAL_FRAMEWORK: [
                PhaseTask(
                    description="Revisar el marco metodologico",
                    instruction=(
                        "Escriba el enfoque metodologico deseado y envie. Luego "
                        "revise el marco metodologico y la matriz de "
                        "conceptualizacion de variables. El archivo es opcional."
                    ),
                )
            ],
            WorkflowPhase.DATA_COLLECTION_INSTRUMENTS: [
                PhaseTask(
                    description="Revisar los instrumentos de recoleccion",
                    instruction=(
                        "Escriba los requisitos de sus instrumentos y envie. Luego "
                        "revise los instrumentos de recoleccion de datos "
                        "propuestos. El archivo es opcional."
                    ),
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

        result: dict[str, Any] = {}
        # Tracks whether the AI produced a response. When False (AI unconfigured)
        # we still persist the user's input and surface an advisory message so
        # the flow is never stuck. The key that carries the displayable AI text
        # per phase; `ai_response` is a shared display field the frontend can
        # always read regardless of phase.
        ai_unconfigured = False

        if phase == WorkflowPhase.PROBLEM_IDENTIFICATION:
            try:
                ai_response = self.ai_service.analyze_problem(user_input, knowledge_context)
            except AIServiceConfigError:
                ai_unconfigured = True
                ai_response = ""
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
            try:
                ai_response = self.ai_service.suggest_instruments(
                    problem or user_input, knowledge_context
                )
            except AIServiceConfigError:
                ai_unconfigured = True
                ai_response = ""
            result = {"suggested_instruments": ai_response, "uploaded_data": user_input}

        elif phase == WorkflowPhase.PROBLEM_REFINEMENT:
            problem = (
                project.problem_description.identified_problem
                if project.problem_description
                else ""
            )
            try:
                ai_response = self.ai_service.refine_problem(
                    problem or "", user_input, knowledge_context
                )
            except AIServiceConfigError:
                ai_unconfigured = True
                ai_response = ""
            result = {"refined_formulations": ai_response}

        elif phase == WorkflowPhase.RESEARCH_QUESTION:
            selected = (
                project.selected_problem.formulation
                if project.selected_problem
                else user_input
            )
            try:
                ai_response = self.ai_service.generate_research_questions(
                    selected, knowledge_context
                )
            except AIServiceConfigError:
                ai_unconfigured = True
                ai_response = ""
            result = {"research_questions": ai_response}

        elif phase == WorkflowPhase.STATE_OF_ART:
            # Handle state-of-art phase: user submits study data
            # Parse the input as a study entry and add to the project's state_of_art
            project_context = self._build_project_context(project)
            try:
                ai_response = self.ai_service.generate_chapter(
                    phase.value, user_input, project_context, knowledge_context
                )
            except AIServiceConfigError:
                ai_unconfigured = True
                ai_response = ""
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
            try:
                ai_response = self.ai_service.generate_chapter(
                    phase.value, user_input, project_context, knowledge_context
                )
            except AIServiceConfigError:
                ai_unconfigured = True
                ai_response = ""
            result = {"generated_content": ai_response}

        # Always persist the user's raw submission so nothing is lost, even when
        # the AI could not respond.
        result["user_input"] = user_input

        # Shared display field the frontend renders for ANY phase. When the AI
        # is unconfigured, carry the advisory message so the user understands
        # why there is no analysis and that their input was still saved.
        if ai_unconfigured:
            result["ai_response"] = ""
            result["ai_unconfigured"] = True
            result["advisory_message"] = AI_UNCONFIGURED_MESSAGE
        else:
            result["ai_response"] = ai_response

        state.phase_data[phase.value] = result

        # Mark the phase's task(s) as completed and attach the AI result so it
        # is inspectable per-task and survives serialization. For phases with a
        # single task this marks that task; for multi-task phases we mark the
        # task(s) satisfied by a text/file submission.
        if state.current_tasks:
            for task in state.current_tasks:
                task.completed = True
                task.response_data = result

        # Auto-run coherence validation so coherence_validated reflects the
        # AI's opinion when an AI is available. This is now ADVISORY only and
        # does not gate advancement (see WorkflowState.can_advance).
        try:
            self.validate_phase_coherence(state, project)
        except Exception:
            # A failing/unconfigured AI must never block the workflow. Leave
            # coherence as-is; advancement is gated on task completion.
            pass

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
