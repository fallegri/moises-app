import { render, screen } from '@testing-library/react'
import { describe, it, expect } from 'vitest'
import PhaseContent from '../components/PhaseContent'
import type { WorkflowStatus, SubmitInputResponse } from '../types/research'

const baseWorkflow: WorkflowStatus = {
  project_id: 'p1',
  current_phase: 'problem_identification',
  phase_info: {
    title: 'Identificacion del Problema',
    description: 'Describe tu problema',
    instruction: 'Escriba en el cuadro de texto una descripcion de la situacion problematica.',
  },
  completed_phases: [],
  current_tasks: [],
  phase_result: null,
  coherence_validated: false,
  last_validation_message: null,
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

  it('does not block advancing on coherence validation (coherence is advisory)', () => {
    // After a submit (persisted or transient) coherence is advisory: no blocked
    // message about validating coherence should ever be shown.
    const submitResult: SubmitInputResponse = {
      phase: 'problem_identification',
      result: {},
      message: 'Input processed successfully',
    }
    renderPhase({ submitResult })
    expect(
      screen.queryByText('Primero valida la coherencia de esta fase')
    ).not.toBeInTheDocument()
    expect(
      screen.queryByText('Primero envia informacion para esta fase')
    ).not.toBeInTheDocument()
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

  it('after advancing to a new phase (no persisted submission), shows the submit message', () => {
    // Simulates the state after handleAdvance: the current phase changed and no
    // submit has happened yet in the new phase (phase_result null, no tasks done).
    const newPhaseWorkflow: WorkflowStatus = {
      ...baseWorkflow,
      current_phase: 'instrument_suggestion',
      phase_info: { title: 'Sugerencia de Instrumentos', description: 'Instrumentos' },
      phase_result: null,
      coherence_validated: false,
      can_advance: false,
    }
    renderPhase({ workflow: newPhaseWorkflow, submitResult: null })
    expect(screen.getByText('Primero envia informacion para esta fase')).toBeInTheDocument()
    expect(
      screen.queryByText('Primero valida la coherencia de esta fase')
    ).not.toBeInTheDocument()
  })

  it('does not render the phase-1 identified-problem block after advancing (no persisted result)', () => {
    const newPhaseWorkflow: WorkflowStatus = {
      ...baseWorkflow,
      current_phase: 'instrument_suggestion',
      phase_result: null,
      coherence_validated: false,
      can_advance: false,
    }
    renderPhase({ workflow: newPhaseWorkflow, submitResult: null })
    expect(screen.queryByText('Problema identificado por la IA')).not.toBeInTheDocument()
  })

  // (a) Persisted AI-identified problem survives reload (submitResult is null).
  it('renders the identified problem from workflow.phase_result when submitResult is null', () => {
    const reloadedWorkflow: WorkflowStatus = {
      ...baseWorkflow,
      phase_result: { identified_problem: 'El problema persistido tras recargar.' },
      can_advance: true,
    }
    renderPhase({ workflow: reloadedWorkflow, submitResult: null })
    expect(screen.getByText('Problema identificado por la IA')).toBeInTheDocument()
    expect(screen.getByText('El problema persistido tras recargar.')).toBeInTheDocument()
  })

  // (b) Saved confirmation shows from persisted data after reload.
  it('shows the saved confirmation from persisted data when submitResult is null', () => {
    const reloadedWorkflow: WorkflowStatus = {
      ...baseWorkflow,
      phase_result: { identified_problem: 'algo' },
      can_advance: true,
    }
    renderPhase({ workflow: reloadedWorkflow, submitResult: null })
    expect(screen.getByText('Informacion guardada exitosamente')).toBeInTheDocument()
  })

  // (c) Advance button enabled / disabled per can_advance.
  it('enables the advance button when can_advance is true and disables it when false', () => {
    const { unmount } = renderPhase({
      workflow: { ...baseWorkflow, can_advance: true },
      submitResult: null,
    })
    expect(screen.getByRole('button', { name: /Avanzar a la siguiente fase/ })).not.toBeDisabled()
    unmount()

    renderPhase({ workflow: { ...baseWorkflow, can_advance: false }, submitResult: null })
    expect(screen.getByRole('button', { name: /Avanzar a la siguiente fase/ })).toBeDisabled()
  })

  // (d) Phase instruction renders.
  it('renders the phase instruction from phase_info', () => {
    renderPhase({ submitResult: null })
    expect(
      screen.getAllByText(
        /Escriba en el cuadro de texto una descripcion de la situacion problematica/
      ).length
    ).toBeGreaterThan(0)
  })

  // (e) Optional-upload note is present.
  it('shows an explicit optional-upload note', () => {
    renderPhase({ submitResult: null })
    expect(screen.getByText(/Opcional/i)).toBeInTheDocument()
  })

  // Task checkbox reflects backend completion after refetch.
  it('renders a checked task checkbox when the backend reports the task completed', () => {
    const workflowWithCompletedTask: WorkflowStatus = {
      ...baseWorkflow,
      current_tasks: [
        { description: 'Describir situacion problematica', instruction: '', completed: true },
      ],
      phase_result: { identified_problem: 'listo' },
      can_advance: true,
    }
    renderPhase({ workflow: workflowWithCompletedTask, submitResult: null })
    const checkbox = screen.getByRole('checkbox') as HTMLInputElement
    expect(checkbox.checked).toBe(true)
  })
})
