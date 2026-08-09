import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import {
  getWorkflowStatus,
  submitInput,
  advanceWorkflow,
  selectOption,
  validateCoherence,
  listProjects,
  createProject,
  deleteProject,
  getProject,
} from '../api/client'
import type { CreateProjectRequest, SelectOptionRequest } from '../types/research'

export function useProjects() {
  return useQuery({
    queryKey: ['projects'],
    queryFn: listProjects,
  })
}

export function useProject(id: string) {
  return useQuery({
    queryKey: ['project', id],
    queryFn: () => getProject(id),
    enabled: !!id,
  })
}

export function useCreateProject() {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: (data: CreateProjectRequest) => createProject(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['projects'] })
    },
  })
}

export function useDeleteProject() {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: (id: string) => deleteProject(id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['projects'] })
    },
  })
}

export function useWorkflowStatus(projectId: string) {
  return useQuery({
    queryKey: ['workflow', projectId],
    queryFn: () => getWorkflowStatus(projectId),
    enabled: !!projectId,
    refetchInterval: false,
  })
}

export function useSubmitInput(projectId: string) {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: ({ text, files }: { text?: string; files?: File[] }) =>
      submitInput(projectId, text, files),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['workflow', projectId] })
    },
  })
}

export function useAdvanceWorkflow(projectId: string) {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: () => advanceWorkflow(projectId),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['workflow', projectId] })
    },
  })
}

export function useSelectOption(projectId: string) {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: (data: SelectOptionRequest) => selectOption(projectId, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['workflow', projectId] })
    },
  })
}

export function useValidateCoherence(projectId: string) {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: () => validateCoherence(projectId),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['workflow', projectId] })
    },
  })
}
