import { Loader2, CheckCircle2, Info, AlertTriangle } from 'lucide-react'
import type { WorkflowStatus, SubmitInputResponse, PhaseId } from '../types/research'
import TextInput from './TextInput'
import FileUpload from './FileUpload'
import AIResponse from './AIResponse'
import StateOfArtMatrix from './StateOfArtMatrix'
import VariableMatrix from './VariableMatrix'

// Per-phase label/placeholder for the free-text box, plus the title shown above
// the persisted AI response, so every phase reads clearly and specifically.
const PHASE_TEXT: Record<PhaseId, { label: string; placeholder: string; responseTitle: string }> = {
  problem_identification: {
    label: 'Describe la situacion problematica',
    placeholder:
      'Ejemplo: En mi empresa la rotacion de personal subio 30% este ano. Incluye antecedentes, cifras, fechas y a quienes afecta...',
    responseTitle: 'Problema identificado por la IA',
  },
  instrument_suggestion: {
    label: 'Resume los datos recopilados con los instrumentos',
    placeholder:
      'Escribe un resumen de los resultados que obtuviste al aplicar encuestas, entrevistas u observaciones...',
    responseTitle: 'Instrumentos sugeridos por la IA',
  },
  problem_refinement: {
    label: 'Datos y hallazgos para reformular el problema',
    placeholder:
      'Escribe los datos o hallazgos que la IA debe considerar para refinar el problema...',
    responseTitle: 'Formulaciones propuestas por la IA',
  },
  research_question: {
    label: 'Aclaraciones o enfoque para la pregunta de investigacion',
    placeholder:
      'Escribe cualquier aclaracion o enfoque que quieras para la pregunta de investigacion...',
    responseTitle: 'Pregunta de investigacion propuesta por la IA',
  },
  introduction: {
    label: 'Ajustes o enfasis para la introduccion',
    placeholder:
      'Escribe los ajustes o el enfasis que deseas para el capitulo de introduccion...',
    responseTitle: 'Introduccion generada por la IA',
  },
  state_of_art: {
    label: 'Sintesis del estado de la cuestion',
    placeholder:
      'Escribe una sintesis del estado de la cuestion a partir de las investigaciones similares registradas...',
    responseTitle: 'Estado de la cuestion generado por la IA',
  },
  problem_identification_chapter: {
    label: 'Ajustes para el capitulo de planteamiento del problema',
    placeholder:
      'Escribe los ajustes que deseas para el capitulo de planteamiento del problema...',
    responseTitle: 'Capitulo de planteamiento generado por la IA',
  },
  specific_problems: {
    label: 'Precisiones para los problemas especificos',
    placeholder: 'Escribe cualquier precision para derivar los problemas especificos...',
    responseTitle: 'Problemas especificos propuestos por la IA',
  },
  research_objective: {
    label: 'Ajustes al enfoque del objetivo de investigacion',
    placeholder: 'Escribe ajustes al enfoque para el objetivo general de investigacion...',
    responseTitle: 'Objetivo de investigacion propuesto por la IA',
  },
  specific_objectives: {
    label: 'Observaciones para los objetivos especificos',
    placeholder: 'Escribe tus observaciones para formular los objetivos especificos...',
    responseTitle: 'Objetivos especificos propuestos por la IA',
  },
  methodological_framework: {
    label: 'Enfoque metodologico deseado',
    placeholder:
      'Escribe el enfoque metodologico deseado y las variables a operacionalizar...',
    responseTitle: 'Marco metodologico generado por la IA',
  },
  data_collection_instruments: {
    label: 'Requisitos de tus instrumentos de recoleccion',
    placeholder:
      'Escribe los requisitos de los instrumentos de recoleccion de datos que necesitas...',
    responseTitle: 'Instrumentos de recoleccion propuestos por la IA',
  },
}

interface PhaseContentProps {
  workflow: WorkflowStatus
  projectId: string
  onSubmitText: (text: string) => void
  onSubmitFiles: (files: File[]) => void
  onSelectOption: (index: number) => void
  onAdvance: () => void
  isSubmitting: boolean
  submitResult?: SubmitInputResponse | null
  advanceError?: string | null
}

export default function PhaseContent({
  workflow,
  projectId,
  onSubmitText,
  onSubmitFiles,
  onSelectOption: _onSelectOption,
  onAdvance,
  isSubmitting,
  submitResult,
  advanceError,
}: PhaseContentProps) {
  const phase = workflow.current_phase
  const phaseCopy = PHASE_TEXT[phase]

  // Persisted phase result from GET /status (survives react-query refetch and
  // page reload), with the transient mutation result as an immediate fallback.
  const phaseResult = workflow.phase_result ?? submitResult?.result ?? null

  const identifiedProblem =
    phaseResult && typeof phaseResult.identified_problem === 'string'
      ? phaseResult.identified_problem
      : ''

  // Whether this phase has been submitted, derived from persisted backend state
  // (phase_result present or any task completed) so it survives reload. Falls
  // back to the transient submitResult for the immediate post-submit render.
  const hasSubmitted =
    phaseResult !== null ||
    (workflow.current_tasks?.some((t) => t.completed) ?? false) ||
    Boolean(submitResult)

  // Advisory shown when the AI was unconfigured at submit time: the input was
  // saved but no analysis could be produced.
  const advisoryMessage =
    phaseResult && phaseResult.ai_unconfigured && typeof phaseResult.advisory_message === 'string'
      ? phaseResult.advisory_message
      : ''

  // Text/markdown AI response for the current phase. The backend exposes a
  // shared `ai_response` display field for every phase; we also fall back to
  // the concrete per-phase keys for robustness (identified_problem is rendered
  // separately in its own highlighted block, so it is excluded here).
  const aiResponseText =
    phaseResult && typeof phaseResult === 'object'
      ? (typeof phaseResult.ai_response === 'string' && phaseResult.ai_response) ||
        (typeof phaseResult.suggested_instruments === 'string' && phaseResult.suggested_instruments) ||
        (typeof phaseResult.refined_formulations === 'string' && phaseResult.refined_formulations) ||
        (typeof phaseResult.research_questions === 'string' && phaseResult.research_questions) ||
        (typeof phaseResult.generated_content === 'string' && phaseResult.generated_content) ||
        ''
      : ''

  // Contextual message explaining why the advance button is disabled. Prefer the
  // backend-provided reason (it also covers phase-specific gates like the
  // state_of_art 6-studies rule) so the UI never enables a button that would 400.
  let advanceBlockedMessage = ''
  if (!workflow.can_advance) {
    advanceBlockedMessage =
      workflow.advance_blocked_reason ||
      (!hasSubmitted ? 'Primero envia informacion para esta fase' : '')
  }

  return (
    <div className="space-y-6">
      {/* Phase info from backend */}
      {workflow.phase_info && (
        <div className="card">
          <h3 className="text-sm font-semibold text-slate-700">{workflow.phase_info.title}</h3>
          <p className="text-sm text-slate-500 mt-1">{workflow.phase_info.description}</p>
          {workflow.phase_info.instruction && (
            <div className="mt-3 rounded-lg border border-blue-100 bg-blue-50 p-3">
              <div className="flex items-start gap-2">
                <Info className="w-4 h-4 text-blue-600 flex-shrink-0 mt-0.5" />
                <div>
                  <p className="text-xs font-semibold text-blue-900 uppercase mb-0.5">
                    Que debes hacer en esta fase
                  </p>
                  <p className="text-sm text-blue-900 whitespace-pre-wrap">
                    {workflow.phase_info.instruction}
                  </p>
                </div>
              </div>
            </div>
          )}
        </div>
      )}

      {/* State of Art Matrix (state_of_art phase) */}
      {phase === 'state_of_art' && (
        <StateOfArtMatrix projectId={projectId} />
      )}

      {/* Variable Matrix (methodological framework) */}
      {phase === 'methodological_framework' && (
        <VariableMatrix projectId={projectId} />
      )}

      {/* Tasks */}
      {workflow.current_tasks && workflow.current_tasks.length > 0 && (
        <div className="card">
          <h3 className="text-sm font-semibold text-slate-700 mb-3">Tareas pendientes</h3>
          <ul className="space-y-2">
            {workflow.current_tasks.map((task, index) => (
              <li key={index} className="flex items-start gap-2">
                <input
                  type="checkbox"
                  checked={task.completed}
                  readOnly
                  className="mt-0.5 rounded border-slate-300"
                />
                <div>
                  <span className={`text-sm ${task.completed ? 'text-slate-400 line-through' : 'text-slate-700'}`}>
                    {task.description}
                  </span>
                  {task.instruction && (
                    <p className="text-xs text-slate-500 mt-0.5">{task.instruction}</p>
                  )}
                </div>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Input Area */}
      <div className="space-y-4">
        <TextInput
          onSubmit={onSubmitText}
          disabled={isSubmitting}
          label={phaseCopy?.label}
          placeholder={phaseCopy?.placeholder}
        />
        <FileUpload
          onFilesAccepted={onSubmitFiles}
          disabled={isSubmitting}
          purpose={workflow.phase_info?.instruction}
        />
      </div>

      {/* Submit confirmation - sourced from persisted workflow data so it
          remains visible after a react-query refetch and page reload. */}
      {hasSubmitted && (
        <div className="rounded-lg border border-green-200 bg-green-50 p-4 space-y-3">
          <div className="flex items-center gap-2">
            <CheckCircle2 className="w-5 h-5 text-green-600 flex-shrink-0" />
            <p className="text-sm font-medium text-green-700">
              {submitResult?.message || 'Informacion guardada exitosamente'}
            </p>
          </div>
          {identifiedProblem && (
            <div className="rounded-lg border border-green-200 bg-white p-3">
              <h4 className="text-xs font-semibold text-slate-500 uppercase mb-1">
                {phaseCopy?.responseTitle || 'Respuesta de la IA'}
              </h4>
              <p className="text-sm text-slate-700 whitespace-pre-wrap">{identifiedProblem}</p>
            </div>
          )}
        </div>
      )}

      {/* Advisory shown when the AI was unconfigured: the input was saved but
          no analysis could be produced, so the flow is not stuck. */}
      {advisoryMessage && (
        <div className="rounded-lg border border-amber-200 bg-amber-50 p-4">
          <div className="flex items-start gap-2">
            <AlertTriangle className="w-5 h-5 text-amber-600 flex-shrink-0 mt-0.5" />
            <p className="text-sm text-amber-800 whitespace-pre-wrap">{advisoryMessage}</p>
          </div>
        </div>
      )}

      {/* AI response rendered as markdown from persisted data. The
          identified_problem is already shown in its own highlighted block
          above, so only render this generic block for the other phases. */}
      {aiResponseText && !identifiedProblem && (
        <div className="space-y-2">
          <h4 className="text-xs font-semibold text-slate-500 uppercase">
            {phaseCopy?.responseTitle || 'Respuesta de la IA'}
          </h4>
          <AIResponse content={aiResponseText} />
        </div>
      )}

      {/* Advance Button */}
      <div className="flex flex-col items-end gap-2 pt-4">
        <button
          onClick={onAdvance}
          disabled={isSubmitting || !workflow.can_advance}
          className="btn-primary flex items-center gap-2"
        >
          {isSubmitting && <Loader2 className="w-4 h-4 animate-spin" />}
          Avanzar a la siguiente fase
        </button>
        {advanceBlockedMessage && (
          <p className="flex items-center gap-1.5 text-sm text-amber-600">
            <Info className="w-4 h-4 flex-shrink-0" />
            {advanceBlockedMessage}
          </p>
        )}
        {advanceError && (
          <p className="flex items-center gap-1.5 text-sm text-red-600">
            <AlertTriangle className="w-4 h-4 flex-shrink-0" />
            {advanceError}
          </p>
        )}
      </div>
    </div>
  )
}
