import { Loader2, CheckCircle2, Info } from 'lucide-react'
import type { WorkflowStatus, SubmitInputResponse } from '../types/research'
import TextInput from './TextInput'
import FileUpload from './FileUpload'
import AIResponse from './AIResponse'
import StateOfArtMatrix from './StateOfArtMatrix'
import VariableMatrix from './VariableMatrix'

interface PhaseContentProps {
  workflow: WorkflowStatus
  projectId: string
  onSubmitText: (text: string) => void
  onSubmitFiles: (files: File[]) => void
  onSelectOption: (index: number) => void
  onAdvance: () => void
  isSubmitting: boolean
  submitResult?: SubmitInputResponse | null
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
}: PhaseContentProps) {
  const phase = workflow.current_phase

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

  // Text/markdown AI response for the current phase, sourced from persisted data.
  const aiResponseText =
    phaseResult && typeof phaseResult === 'object'
      ? (typeof phaseResult.response === 'string' && phaseResult.response) ||
        (typeof phaseResult.content === 'string' && phaseResult.content) ||
        (typeof phaseResult.text === 'string' && phaseResult.text) ||
        ''
      : ''

  // Contextual message explaining why the advance button is disabled. Reads from
  // the persisted workflow status: when can_advance is true, show nothing.
  let advanceBlockedMessage = ''
  if (!workflow.can_advance) {
    if (!hasSubmitted) {
      advanceBlockedMessage = 'Primero envia informacion para esta fase'
    }
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
        <TextInput onSubmit={onSubmitText} disabled={isSubmitting} />
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
                Problema identificado por la IA
              </h4>
              <p className="text-sm text-slate-700 whitespace-pre-wrap">{identifiedProblem}</p>
            </div>
          )}
        </div>
      )}

      {/* AI response rendered as markdown from persisted data */}
      {aiResponseText && <AIResponse content={aiResponseText} />}

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
      </div>
    </div>
  )
}
