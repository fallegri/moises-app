import { render, screen, waitFor, fireEvent } from '@testing-library/react'
import { describe, it, expect, vi, beforeEach } from 'vitest'
import KnowledgeBase from '../components/KnowledgeBase'
import * as client from '../api/client'

vi.mock('../api/client', () => ({
  getKnowledgeDocuments: vi.fn(),
  uploadKnowledge: vi.fn(),
  searchKnowledge: vi.fn(),
}))

const mockedClient = vi.mocked(client)

describe('KnowledgeBase', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('renders the list of already-uploaded documents on mount', async () => {
    mockedClient.getKnowledgeDocuments.mockResolvedValue({
      documents: ['paper1.md', 'notes.txt'],
      total: 2,
    })

    render(<KnowledgeBase />)

    await waitFor(() => {
      expect(screen.getByText('paper1.md')).toBeInTheDocument()
    })
    expect(screen.getByText('notes.txt')).toBeInTheDocument()
    expect(screen.getByText('Documentos cargados (2)')).toBeInTheDocument()
  })

  it('shows an empty state when there are no documents', async () => {
    mockedClient.getKnowledgeDocuments.mockResolvedValue({ documents: [], total: 0 })

    render(<KnowledgeBase />)

    await waitFor(() => {
      expect(screen.getByText('Aun no se han cargado documentos.')).toBeInTheDocument()
    })
  })

  it('uploads every selected file in a multi-file selection and refreshes the list', async () => {
    mockedClient.getKnowledgeDocuments
      .mockResolvedValueOnce({ documents: [], total: 0 })
      .mockResolvedValue({ documents: ['a.md', 'b.md'], total: 2 })
    mockedClient.uploadKnowledge.mockResolvedValue({ message: 'ok' })

    const { container } = render(<KnowledgeBase />)
    await waitFor(() => {
      expect(screen.getByText('Aun no se han cargado documentos.')).toBeInTheDocument()
    })

    const input = container.querySelector('input[type="file"]') as HTMLInputElement
    const fileA = new File(['a'], 'a.md', { type: 'text/markdown' })
    const fileB = new File(['b'], 'b.md', { type: 'text/markdown' })

    fireEvent.change(input, { target: { files: [fileA, fileB] } })

    await waitFor(() => {
      expect(mockedClient.uploadKnowledge).toHaveBeenCalledTimes(2)
    })
    expect(screen.getByText('2 archivos subidos exitosamente')).toBeInTheDocument()
    // list refreshed: initial mount + after upload
    await waitFor(() => {
      expect(screen.getByText('a.md')).toBeInTheDocument()
    })
  })

  it('on partial failure reports counts and still refreshes the document list', async () => {
    mockedClient.getKnowledgeDocuments
      .mockResolvedValueOnce({ documents: [], total: 0 })
      .mockResolvedValue({ documents: ['ok.md'], total: 1 })
    mockedClient.uploadKnowledge
      .mockResolvedValueOnce({ message: 'ok' })
      .mockRejectedValueOnce(new Error('boom'))

    const { container } = render(<KnowledgeBase />)
    await waitFor(() => {
      expect(screen.getByText('Aun no se han cargado documentos.')).toBeInTheDocument()
    })

    const input = container.querySelector('input[type="file"]') as HTMLInputElement
    const good = new File(['a'], 'ok.md', { type: 'text/markdown' })
    const bad = new File(['b'], 'bad.md', { type: 'text/markdown' })

    fireEvent.change(input, { target: { files: [good, bad] } })

    await waitFor(() => {
      expect(mockedClient.uploadKnowledge).toHaveBeenCalledTimes(2)
    })
    expect(screen.getByText('1 subidos, 1 fallaron')).toBeInTheDocument()
    // list still refreshed despite the failure
    await waitFor(() => {
      expect(screen.getByText('ok.md')).toBeInTheDocument()
    })
  })
})
