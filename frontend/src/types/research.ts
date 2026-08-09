export type PhaseId =
  | 'problem_identification'
  | 'instrument_suggestion'
  | 'problem_refinement'
  | 'research_question'
  | 'introduction'
  | 'background'
  | 'problem_chapter'
  | 'specific_problems'
  | 'research_objective'
  | 'specific_objectives'
  | 'methodological_framework'
  | 'data_collection'

export interface Phase {
  id: PhaseId
  name: string
  description: string
  status: 'completed' | 'current' | 'upcoming'
}

export interface Task {
  id: string
  description: string
  completed: boolean
}

export interface WorkflowStatus {
  project_id: string
  current_phase: PhaseId
  phases: Phase[]
  tasks: Task[]
  progress: number
  ai_response?: string
  options?: string[]
}

export interface ResearchProject {
  id: string
  title: string
  description: string
  created_at: string
  updated_at: string
  current_phase: PhaseId
  progress: number
}

export interface CreateProjectRequest {
  title: string
  description: string
}

export interface SubmitInputRequest {
  text?: string
  files?: File[]
}

export interface SelectOptionRequest {
  option_index: number
}

export interface ValidationResult {
  is_valid: boolean
  score: number
  issues: string[]
  suggestions: string[]
}

export interface DocumentInfo {
  chapter: string
  title: string
  generated: boolean
  download_url?: string
}

export interface KnowledgeDocument {
  id: string
  title: string
  content_preview: string
}

export interface StudyEntry {
  id: string
  author: string
  year: string
  title: string
  methodology: string
  findings: string
  relevance: string
}

export interface VariableEntry {
  id: string
  variable: string
  dimensions: string
  indicators: string
  instruments: string
}

export const PHASES: { id: PhaseId; name: string; description: string }[] = [
  { id: 'problem_identification', name: 'Identificacion del Problema', description: 'Presenta los antecedentes de la situacion problematica' },
  { id: 'instrument_suggestion', name: 'Sugerencia de Instrumentos', description: 'Instrumentos para identificar mejor el problema' },
  { id: 'problem_refinement', name: 'Refinamiento del Problema', description: 'Selecciona entre 3 formulaciones del problema' },
  { id: 'research_question', name: 'Pregunta de Investigacion', description: 'Identificacion de la pregunta de investigacion' },
  { id: 'introduction', name: 'Introduccion', description: 'Construccion del capitulo de introduccion' },
  { id: 'background', name: 'Antecedentes', description: 'Estado de la cuestion con matriz de investigaciones' },
  { id: 'problem_chapter', name: 'Capitulo del Problema', description: 'Redaccion del capitulo de identificacion del problema' },
  { id: 'specific_problems', name: 'Problemas Especificos', description: 'Identificacion de problemas especificos' },
  { id: 'research_objective', name: 'Objetivo de Investigacion', description: 'Definicion del objetivo general' },
  { id: 'specific_objectives', name: 'Objetivos Especificos', description: 'Definicion de objetivos especificos' },
  { id: 'methodological_framework', name: 'Marco Metodologico', description: 'Matriz de conceptualizacion de variables' },
  { id: 'data_collection', name: 'Recopilacion de Datos', description: 'Instrumentos de recopilacion de informacion' },
]
