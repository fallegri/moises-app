import { CheckCircle2, Circle, CircleDot } from 'lucide-react'
import type { Phase } from '../types/research'

interface WorkflowStepperProps {
  phases: Phase[]
  onPhaseClick?: (phaseId: string) => void
}

export default function WorkflowStepper({ phases, onPhaseClick }: WorkflowStepperProps) {
  return (
    <nav className="space-y-1" aria-label="Fases del flujo de trabajo">
      {phases.map((phase, index) => {
        const isLast = index === phases.length - 1

        return (
          <div key={phase.id} className="relative">
            <button
              onClick={() => onPhaseClick?.(phase.id)}
              className={`w-full flex items-start gap-3 px-3 py-2.5 rounded-lg text-left transition-colors ${
                phase.status === 'current'
                  ? 'bg-blue-50 border border-blue-200'
                  : phase.status === 'completed'
                  ? 'hover:bg-slate-50'
                  : 'opacity-60'
              }`}
              disabled={phase.status === 'upcoming'}
            >
              <div className="flex-shrink-0 mt-0.5">
                {phase.status === 'completed' && (
                  <CheckCircle2 className="w-5 h-5 text-green-600" />
                )}
                {phase.status === 'current' && (
                  <CircleDot className="w-5 h-5 text-blue-600" />
                )}
                {phase.status === 'upcoming' && (
                  <Circle className="w-5 h-5 text-slate-300" />
                )}
              </div>
              <div className="min-w-0 flex-1">
                <p
                  className={`text-sm font-medium truncate ${
                    phase.status === 'current'
                      ? 'text-blue-900'
                      : phase.status === 'completed'
                      ? 'text-slate-700'
                      : 'text-slate-400'
                  }`}
                >
                  {phase.name}
                </p>
                {phase.status === 'current' && (
                  <p className="text-xs text-blue-600 mt-0.5">{phase.description}</p>
                )}
              </div>
            </button>
            {!isLast && (
              <div className="absolute left-[22px] top-[38px] w-0.5 h-2 bg-slate-200" />
            )}
          </div>
        )
      })}
    </nav>
  )
}
