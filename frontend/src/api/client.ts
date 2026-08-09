import axios from 'axios'
import type {
  ResearchProject,
  CreateProjectRequest,
  WorkflowStatus,
  SelectOptionRequest,
  ValidationResult,
  KnowledgeSearchResult,
} from '../types/research'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || '',
  headers: {
    'Content-Type': 'application/json',
  },
})

// Projects
export async function createProject(data: CreateProjectRequest): Promise<ResearchProject> {
  const response = await api.post('/api/projects', data)
  return response.data
}

export async function listProjects(): Promise<ResearchProject[]> {
  const response = await api.get('/api/projects')
  return response.data
}

export async function getProject(id: string): Promise<ResearchProject> {
  const response = await api.get(`/api/projects/${id}`)
  return response.data
}

export async function deleteProject(id: string): Promise<void> {
  await api.delete(`/api/projects/${id}`)
}

// Workflow
export async function getWorkflowStatus(projectId: string): Promise<WorkflowStatus> {
  const response = await api.get(`/api/workflow/${projectId}/status`)
  return response.data
}

export async function submitInput(projectId: string, text?: string, files?: File[]): Promise<WorkflowStatus> {
  let fileContent: string | undefined
  if (files && files.length > 0) {
    // Read file contents as text to send alongside user text
    const fileTexts: string[] = []
    for (const file of files) {
      const content = await file.text()
      fileTexts.push(`[${file.name}]\n${content}`)
    }
    fileContent = fileTexts.join('\n\n')
  }
  const response = await api.post(`/api/workflow/${projectId}/submit-input`, {
    text: text || '',
    file_content: fileContent,
  })
  return response.data
}

export async function advanceWorkflow(projectId: string): Promise<WorkflowStatus> {
  const response = await api.post(`/api/workflow/${projectId}/advance`)
  return response.data
}

export async function selectOption(projectId: string, data: SelectOptionRequest): Promise<WorkflowStatus> {
  const response = await api.post(`/api/workflow/${projectId}/select-option`, data)
  return response.data
}

export async function validateCoherence(projectId: string): Promise<ValidationResult> {
  const response = await api.post(`/api/workflow/${projectId}/validate`)
  return response.data
}

// State of Art
export interface AddStudyData {
  title: string
  authors: string
  year: number
  methodology: string
  findings: string
  relevance: string
  source?: string
}

export async function addStudy(projectId: string, data: AddStudyData): Promise<{ message: string }> {
  const response = await api.post(`/api/workflow/${projectId}/state-of-art/add-study`, data)
  return response.data
}

export async function setNoMoreStudies(projectId: string, noMoreStudies: boolean): Promise<{ message: string }> {
  const response = await api.post(`/api/workflow/${projectId}/state-of-art/no-more-studies`, {
    no_more_studies_found: noMoreStudies,
  })
  return response.data
}

// Documents
export async function generateDocument(projectId: string, chapter: string): Promise<{ message: string }> {
  const response = await api.post(`/api/documents/${projectId}/generate/${chapter}`)
  return response.data
}

export function getDocumentDownloadUrl(projectId: string, chapter: string): string {
  const baseUrl = import.meta.env.VITE_API_URL || ''
  return `${baseUrl}/api/documents/${projectId}/download/${chapter}`
}

// Knowledge Base
export async function searchKnowledge(query: string): Promise<KnowledgeSearchResult[]> {
  const response = await api.get('/api/knowledge/search', { params: { q: query } })
  return response.data.results
}

export async function uploadKnowledge(file: File): Promise<{ message: string }> {
  const formData = new FormData()
  formData.append('file', file)
  const response = await api.post('/api/knowledge/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
  return response.data
}
