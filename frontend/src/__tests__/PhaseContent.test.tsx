import { render, screen } from '@testing-library/react'
import { describe, it, expect } from 'vitest'
import PhaseContent from '../components/PhaseContent'
import type { WorkflowStatus, SubmitInputResponse } from '../types/research'

const baseWorkflow: WorkflowStatus = {
  project_id: 'p1',
  current_phase: 'problem_identification',
  phase_info: { title: 'Identificacion del Problema', description: 'Describe tu problema' },
  completed_phases: [],
  current_tasks: [],
  coherence_validated: false,
  can_advance: false,
}

const noop = () => {}

function renderPhase(overrides: Partial<React.ComponentProps<typeof PhaseContent>> = {}) {
  return render(
    <PhaseContent
      workflow={baseWorkflow}
      projectId="p1"
      onSubmitText={noop}
      onSubmitFiles={noop}
      onSelectOption={noop}
      onAdvance={noop}
      isSubmitting={false}
      {...overrides}
    />
  )
}

describe('PhaseContent', () => {
  it('shows message to submit info when nothing submitted and cannot advance', () => {
    renderPhase({ submitResult: null })
    expect(screen.getByText('Primero envia informacion para esta fase')).toBeInTheDocument()
  })

  it('shows message to validate coherence after submit when coherence not validated', () => {
    const submitResult: SubmitInputResponse = {
      phase: 'problem_identification',
      result: {},
      message: 'Input processed successfully',
    }
    renderPhase({ submitResult })
    expect(screen.getByText('Primero valida la coherencia de esta fase')).toBeInTheDocument()
  })

  it('shows success confirmation with message after submit', () => {
    const submitResult: SubmitInputResponse = {
      phase: 'problem_identification',
      result: {},
      message: 'Input processed successfully',
    }
    renderPhase({ submitResult })
    expect(screen.getByText('Input processed successfully')).toBeInTheDocument()
  })

  it('displays AI-identified problem when present in result', () => {
    const submitResult: SubmitInputResponse = {
      phase: 'problem_identification',
      result: { identified_problem: 'El problema es la falta de datos.' },
      message: 'Input processed successfully',
    }
    renderPhase({ submitResult })
    expect(screen.getByText('Problema identificado por la IA')).toBeInTheDocument()
    expect(screen.getByText('El problema es la falta de datos.')).toBeInTheDocument()
  })

  it('does not show a blocked message when can_advance is true', () => {
    renderPhase({ workflow: { ...baseWorkflow, can_advance: true } })
    expect(screen.queryByText('Primero envia informacion para esta fase')).not.toBeInTheDocument()
    expect(screen.queryByText('Primero valida la coherencia de esta fase')).not.toBeInTheDocument()
  })
})
