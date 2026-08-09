import { useParams, Link } from 'react-router-dom'
import { Loader2, FileText, AlertCircle } from 'lucide-react'
import WorkflowStepper from '../components/WorkflowStepper'
import PhaseContent from '../components/PhaseContent'
import CoherenceValidation from '../components/CoherenceValidation'
import KnowledgeBase from '../components/KnowledgeBase'
import {
  useProject,
  useWorkflowStatus,
  useSubmitInput,
  useSelectOption,
  useAdvanceWorkflow,
  useValidateCoherence,
} from '../hooks/useWorkflow'
import { PHASES } from '../types/research'
import type { Phase, ValidationResult } from '../types/research'
import { useState } from 'react'

export default function Project() {
  const { id } = useParams<{ id: string }>()
  const { data: project, isLoading: projectLoading } = useProject(id!)
  const { data: workflow, isLoading: workflowLoading, error: workflowError } = useWorkflowStatus(id!)
  const submitInput = useSubmitInput(id!)
  const selectOption = useSelectOption(id!)
  const advanceWorkflow = useAdvanceWorkflow(id!)
  const validateCoherence = useValidateCoherence(id!)
  const [validationResult, setValidationResult] = useState<ValidationResult | null>(null)

  if (projectLoading || workflowLoading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="text-center">
          <Loader2 className="w-8 h-8 animate-spin text-blue-600 mx-auto" />
          <p className="text-sm text-slate-500 mt-3">Cargando proyecto...</p>
        </div>
      </div>
    )
  }

  if (workflowError) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="text-center card max-w-md">
          <AlertCircle className="w-10 h-10 text-red-500 mx-auto mb-3" />
          <h2 className="text-lg font-semibold text-slate-800">Error al cargar el proyecto</h2>
          <p className="text-sm text-slate-500 mt-1">
            No se pudo conectar con el servidor. Verifica que el backend este ejecutandose.
          </p>
          <Link to="/" className="btn-primary mt-4 inline-block">
            Volver al inicio
          </Link>
        </div>
      </div>
    )
  }

  const phases: Phase[] = PHASES.map((p) => {
    let status: Phase['status'] = 'upcoming'
    if (workflow) {
      const currentIndex = PHASES.findIndex((ph) => ph.id === workflow.current_phase)
      const thisIndex = PHASES.findIndex((ph) => ph.id === p.id)
      if (thisIndex < currentIndex) status = 'completed'
      else if (thisIndex === currentIndex) status = 'current'
    }
    return { ...p, status }
  })

  const currentPhaseName = PHASES.find((p) => p.id === workflow?.current_phase)?.name || ''

  const handleSubmitText = (text: string) => {
    submitInput.mutate({ text })
  }

  const handleSubmitFiles = (files: File[]) => {
    submitInput.mutate({ files })
  }

  const handleSelectOption = (index: number) => {
    selectOption.mutate({ option_index: index })
  }

  const handleAdvance = () => {
    advanceWorkflow.mutate()
  }

  const handleValidate = async () => {
    const result = await validateCoherence.mutateAsync()
    setValidationResult(result)
  }

  const isSubmitting =
    submitInput.isPending || selectOption.isPending || advanceWorkflow.isPending

  return (
    <div className="flex h-[calc(100vh-73px)]">
      {/* Sidebar */}
      <aside className="w-72 bg-white border-r border-slate-200 overflow-y-auto p-4 flex-shrink-0">
        <div className="mb-4 pb-3 border-b border-slate-200">
          <h2 className="text-sm font-bold text-slate-900 truncate">
            {project?.title || 'Proyecto'}
          </h2>
          {workflow && (
            <div className="flex items-center gap-2 mt-2">
              <div className="flex-1 h-1.5 bg-slate-200 rounded-full overflow-hidden">
                <div
                  className="h-full bg-blue-500 rounded-full transition-all"
                  style={{ width: `${workflow.progress}%` }}
                />
              </div>
              <span className="text-xs text-slate-500">{workflow.progress}%</span>
            </div>
          )}
        </div>
        <WorkflowStepper phases={phases} />
        <div className="mt-4 pt-4 border-t border-slate-200">
          <Link
            to={`/project/${id}/documents`}
            className="flex items-center gap-2 px-3 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg transition-colors"
          >
            <FileText className="w-4 h-4" />
            Ver Documentos
          </Link>
        </div>
      </aside>

      {/* Main Content */}
      <div className="flex-1 overflow-y-auto">
        <div className="max-w-3xl mx-auto px-6 py-8">
          {/* Phase Header */}
          <div className="mb-6">
            <h1 className="text-2xl font-bold text-slate-900">{currentPhaseName}</h1>
            <p className="text-sm text-slate-500 mt-1">
              {PHASES.find((p) => p.id === workflow?.current_phase)?.description}
            </p>
          </div>

          {/* Phase Content */}
          {workflow && (
            <PhaseContent
              workflow={workflow}
              onSubmitText={handleSubmitText}
              onSubmitFiles={handleSubmitFiles}
              onSelectOption={handleSelectOption}
              onAdvance={handleAdvance}
              isSubmitting={isSubmitting}
            />
          )}

          {/* Validation */}
          <div className="mt-6 space-y-4">
            <button
              onClick={handleValidate}
              disabled={validateCoherence.isPending}
              className="btn-secondary flex items-center gap-2 text-sm"
            >
              {validateCoherence.isPending && <Loader2 className="w-4 h-4 animate-spin" />}
              Validar Coherencia
            </button>
            {validationResult && <CoherenceValidation result={validationResult} />}
          </div>

          {/* Knowledge Base */}
          <div className="mt-8">
            <KnowledgeBase />
          </div>
        </div>
      </div>
    </div>
  )
}
