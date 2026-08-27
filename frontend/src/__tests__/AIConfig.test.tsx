import { render, screen, waitFor, fireEvent } from '@testing-library/react'
import { describe, it, expect, vi, beforeEach } from 'vitest'
import AIConfig from '../components/AIConfig'
import * as client from '../api/client'

vi.mock('../api/client', () => ({
  getAIConfig: vi.fn(),
  updateAIConfig: vi.fn(),
}))

const mockedClient = vi.mocked(client)

const NVIDIA_BASE_URL = 'https://integrate.api.nvidia.com/v1'

describe('AIConfig', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('shows the model field prominently with NVIDIA example models', async () => {
    mockedClient.getAIConfig.mockResolvedValue({
      api_key_masked: '',
      base_url: NVIDIA_BASE_URL,
      model: 'meta/llama-3.1-405b-instruct',
      is_configured: false,
    })

    render(<AIConfig />)

    await waitFor(() => {
      expect(screen.getByText('Modelo')).toBeInTheDocument()
    })
    expect(
      screen.getByPlaceholderText('deepseek-ai/deepseek-v4-pro-0813')
    ).toBeInTheDocument()
    expect(
      screen.getByText(/Ejemplos: deepseek-ai\/deepseek-v4-pro-0813, meta\/llama-3.1-405b-instruct/)
    ).toBeInTheDocument()
    // Helper note explaining the NVIDIA endpoint is common
    expect(
      screen.getByText(/Todos los modelos usan el endpoint de NVIDIA/)
    ).toBeInTheDocument()
  })

  it('keeps the Base URL field hidden behind advanced options by default', async () => {
    mockedClient.getAIConfig.mockResolvedValue({
      api_key_masked: '',
      base_url: NVIDIA_BASE_URL,
      model: '',
      is_configured: false,
    })

    render(<AIConfig />)

    await waitFor(() => {
      expect(screen.getByText('Opciones avanzadas')).toBeInTheDocument()
    })
    expect(screen.queryByText('Base URL')).not.toBeInTheDocument()

    fireEvent.click(screen.getByText('Opciones avanzadas'))

    expect(screen.getByText('Base URL')).toBeInTheDocument()
  })

  it('always sends the NVIDIA base URL when saving, even if it was never touched', async () => {
    mockedClient.getAIConfig.mockResolvedValue({
      api_key_masked: '',
      base_url: NVIDIA_BASE_URL,
      model: '',
      is_configured: false,
    })
    mockedClient.updateAIConfig.mockResolvedValue({
      api_key_masked: '****abcd',
      base_url: NVIDIA_BASE_URL,
      model: 'deepseek-ai/deepseek-v4-pro-0813',
      is_configured: true,
    })

    render(<AIConfig />)

    await waitFor(() => {
      expect(screen.getByText('Modelo')).toBeInTheDocument()
    })

    fireEvent.change(screen.getByPlaceholderText('deepseek-ai/deepseek-v4-pro-0813'), {
      target: { value: 'deepseek-ai/deepseek-v4-pro-0813' },
    })
    fireEvent.change(screen.getByPlaceholderText('Ingresa tu API key'), {
      target: { value: 'nvapi-secret' },
    })
    fireEvent.click(screen.getByText('Guardar Configuracion'))

    await waitFor(() => {
      expect(mockedClient.updateAIConfig).toHaveBeenCalledWith({
        api_key: 'nvapi-secret',
        base_url: NVIDIA_BASE_URL,
        model: 'deepseek-ai/deepseek-v4-pro-0813',
      })
    })
    expect(
      screen.getByText('Configuracion guardada exitosamente')
    ).toBeInTheDocument()
  })

  it('defaults the base URL to the NVIDIA endpoint when the backend returns none', async () => {
    mockedClient.getAIConfig.mockResolvedValue({
      api_key_masked: '',
      base_url: '',
      model: 'meta/llama-3.1-405b-instruct',
      is_configured: false,
    })
    mockedClient.updateAIConfig.mockResolvedValue({
      api_key_masked: '',
      base_url: NVIDIA_BASE_URL,
      model: 'meta/llama-3.1-405b-instruct',
      is_configured: false,
    })

    render(<AIConfig />)

    await waitFor(() => {
      expect(screen.getByText('Opciones avanzadas')).toBeInTheDocument()
    })
    fireEvent.click(screen.getByText('Opciones avanzadas'))

    const baseUrlInput = screen.getByPlaceholderText(NVIDIA_BASE_URL) as HTMLInputElement
    expect(baseUrlInput.value).toBe(NVIDIA_BASE_URL)
  })
})
