import { Loader2, CheckCircle2, Info } from 'lucide-react'
import type { WorkflowStatus, SubmitInputResponse } from '../types/research'
import TextInput from './TextInput'
import FileUpload from './FileUpload'
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
  const identifiedProblem =
    submitResult?.result && typeof submitResult.result.identified_problem === 'string'
      ? submitResult.result.identified_problem
      : ''

  // Contextual message explaining why the advance button is disabled
  let advanceBlockedMessage = ''
  if (!workflow.can_advance) {
    if (submitResult && !workflow.coherence_validated) {
      advanceBlockedMessage = 'Primero valida la coherencia de esta fase'
    } else if (!submitResult) {
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
        <FileUpload onFilesAccepted={onSubmitFiles} disabled={isSubmitting} />
      </div>

      {/* Submit success confirmation */}
      {submitResult && (
        <div className="rounded-lg border border-green-200 bg-green-50 p-4 space-y-3">
          <div className="flex items-center gap-2">
            <CheckCircle2 className="w-5 h-5 text-green-600 flex-shrink-0" />
            <p className="text-sm font-medium text-green-700">
              {submitResult.message || 'Informacion guardada exitosamente'}
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
