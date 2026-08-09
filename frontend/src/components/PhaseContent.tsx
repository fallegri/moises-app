import { Loader2 } from 'lucide-react'
import type { WorkflowStatus } from '../types/research'
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
}

export default function PhaseContent({
  workflow,
  projectId,
  onSubmitText,
  onSubmitFiles,
  onSelectOption: _onSelectOption,
  onAdvance,
  isSubmitting,
}: PhaseContentProps) {
  const phase = workflow.current_phase

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
        <VariableMatrix />
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

      {/* Advance Button */}
      <div className="flex justify-end pt-4">
        <button
          onClick={onAdvance}
          disabled={isSubmitting || !workflow.can_advance}
          className="btn-primary flex items-center gap-2"
        >
          {isSubmitting && <Loader2 className="w-4 h-4 animate-spin" />}
          Avanzar a la siguiente fase
        </button>
      </div>
    </div>
  )
}
