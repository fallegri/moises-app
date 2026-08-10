import { render, screen } from '@testing-library/react'
import { describe, it, expect } from 'vitest'
import WorkflowStepper from '../components/WorkflowStepper'
import type { Phase } from '../types/research'

const mockPhases: Phase[] = [
  { id: 'problem_identification', name: 'Identificacion del Problema', description: 'Describe tu situacion', status: 'completed' },
  { id: 'instrument_suggestion', name: 'Sugerencia de Instrumentos', description: 'Instrumentos para el problema', status: 'current' },
  { id: 'problem_refinement', name: 'Refinamiento del Problema', description: 'Selecciona formulacion', status: 'upcoming' },
  { id: 'research_question', name: 'Pregunta de Investigacion', description: 'Identifica la pregunta', status: 'upcoming' },
]

describe('WorkflowStepper', () => {
  it('renders all phase names', () => {
    render(<WorkflowStepper phases={mockPhases} />)
    expect(screen.getByText('Identificacion del Problema')).toBeInTheDocument()
    expect(screen.getByText('Sugerencia de Instrumentos')).toBeInTheDocument()
    expect(screen.getByText('Refinamiento del Problema')).toBeInTheDocument()
    expect(screen.getByText('Pregunta de Investigacion')).toBeInTheDocument()
  })

  it('shows description for current phase', () => {
    render(<WorkflowStepper phases={mockPhases} />)
    expect(screen.getByText('Instrumentos para el problema')).toBeInTheDocument()
  })

  it('does not show description for completed phases', () => {
    render(<WorkflowStepper phases={mockPhases} />)
    expect(screen.queryByText('Describe tu situacion')).not.toBeInTheDocument()
  })

  it('does not show description for upcoming phases', () => {
    render(<WorkflowStepper phases={mockPhases} />)
    expect(screen.queryByText('Selecciona formulacion')).not.toBeInTheDocument()
    expect(screen.queryByText('Identifica la pregunta')).not.toBeInTheDocument()
  })

  it('disables upcoming phase buttons', () => {
    render(<WorkflowStepper phases={mockPhases} />)
    const upcomingButtons = screen.getAllByRole('button')
    // Third and fourth buttons should be disabled
    expect(upcomingButtons[2]).toBeDisabled()
    expect(upcomingButtons[3]).toBeDisabled()
  })

  it('enables completed and current phase buttons', () => {
    render(<WorkflowStepper phases={mockPhases} />)
    const buttons = screen.getAllByRole('button')
    expect(buttons[0]).not.toBeDisabled()
    expect(buttons[1]).not.toBeDisabled()
  })
})
