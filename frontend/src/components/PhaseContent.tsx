import { Loader2 } from 'lucide-react'
import type { WorkflowStatus } from '../types/research'
import TextInput from './TextInput'
import FileUpload from './FileUpload'
import AIResponse from './AIResponse'
import OptionSelector from './OptionSelector'
import StateOfArtMatrix from './StateOfArtMatrix'
import VariableMatrix from './VariableMatrix'

interface PhaseContentProps {
  workflow: WorkflowStatus
  onSubmitText: (text: string) => void
  onSubmitFiles: (files: File[]) => void
  onSelectOption: (index: number) => void
  onAdvance: () => void
  isSubmitting: boolean
}

export default function PhaseContent({
  workflow,
  onSubmitText,
  onSubmitFiles,
  onSelectOption,
  onAdvance,
  isSubmitting,
}: PhaseContentProps) {
  const phase = workflow.current_phase

  return (
    <div className="space-y-6">
      {/* AI Response */}
      {workflow.ai_response && (
        <AIResponse content={workflow.ai_response} />
      )}

      {/* Options (e.g., 3 problem formulations) */}
      {workflow.options && workflow.options.length > 0 && (
        <OptionSelector
          options={workflow.options}
          onSelect={onSelectOption}
          disabled={isSubmitting}
        />
      )}

      {/* State of Art Matrix (background phase) */}
      {phase === 'background' && (
        <StateOfArtMatrix />
      )}

      {/* Variable Matrix (methodological framework) */}
      {phase === 'methodological_framework' && (
        <VariableMatrix />
      )}

      {/* Tasks */}
      {workflow.tasks && workflow.tasks.length > 0 && (
        <div className="card">
          <h3 className="text-sm font-semibold text-slate-700 mb-3">Tareas pendientes</h3>
          <ul className="space-y-2">
            {workflow.tasks.map((task) => (
              <li key={task.id} className="flex items-start gap-2">
                <input
                  type="checkbox"
                  checked={task.completed}
                  readOnly
                  className="mt-0.5 rounded border-slate-300"
                />
                <span className={`text-sm ${task.completed ? 'text-slate-400 line-through' : 'text-slate-700'}`}>
                  {task.description}
                </span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Input Area */}
      {!workflow.options?.length && (
        <div className="space-y-4">
          <TextInput onSubmit={onSubmitText} disabled={isSubmitting} />
          <FileUpload onFilesAccepted={onSubmitFiles} disabled={isSubmitting} />
        </div>
      )}

      {/* Advance Button */}
      <div className="flex justify-end pt-4">
        <button
          onClick={onAdvance}
          disabled={isSubmitting}
          className="btn-primary flex items-center gap-2"
        >
          {isSubmitting && <Loader2 className="w-4 h-4 animate-spin" />}
          Avanzar a la siguiente fase
        </button>
      </div>
    </div>
  )
}
