export type PhaseId =
  | 'problem_identification'
  | 'instrument_suggestion'
  | 'problem_refinement'
  | 'research_question'
  | 'introduction'
  | 'state_of_art'
  | 'problem_identification_chapter'
  | 'specific_problems'
  | 'research_objective'
  | 'specific_objectives'
  | 'methodological_framework'
  | 'data_collection_instruments'

export interface Phase {
  id: PhaseId
  name: string
  description: string
  status: 'completed' | 'current' | 'upcoming'
}

export interface Task {
  description: string
  instruction: string
  completed: boolean
}

export interface WorkflowStatus {
  project_id: string
  current_phase: PhaseId
  phase_info: { title: string; description: string }
  completed_phases: PhaseId[]
  current_tasks: Task[]
  coherence_validated: boolean
  can_advance: boolean
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

export interface KnowledgeSearchResult {
  filename: string
  heading: string
  content: string
  score: number
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
  { id: 'state_of_art', name: 'Antecedentes', description: 'Estado de la cuestion con matriz de investigaciones' },
  { id: 'problem_identification_chapter', name: 'Capitulo del Problema', description: 'Redaccion del capitulo de identificacion del problema' },
  { id: 'specific_problems', name: 'Problemas Especificos', description: 'Identificacion de problemas especificos' },
  { id: 'research_objective', name: 'Objetivo de Investigacion', description: 'Definicion del objetivo general' },
  { id: 'specific_objectives', name: 'Objetivos Especificos', description: 'Definicion de objetivos especificos' },
  { id: 'methodological_framework', name: 'Marco Metodologico', description: 'Matriz de conceptualizacion de variables' },
  { id: 'data_collection_instruments', name: 'Recopilacion de Datos', description: 'Instrumentos de recopilacion de informacion' },
]
