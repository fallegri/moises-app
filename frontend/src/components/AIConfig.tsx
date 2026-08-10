import { useState, useEffect } from 'react'
import { Settings, Eye, EyeOff, Check, AlertCircle } from 'lucide-react'
import { getAIConfig, updateAIConfig } from '../api/client'
import type { AIConfig as AIConfigType } from '../types/research'

export default function AIConfig() {
  const [config, setConfig] = useState<AIConfigType | null>(null)
  const [apiKey, setApiKey] = useState('')
  const [baseUrl, setBaseUrl] = useState('')
  const [model, setModel] = useState('')
  const [showKey, setShowKey] = useState(false)
  const [saving, setSaving] = useState(false)
  const [message, setMessage] = useState<{ type: 'success' | 'error'; text: string } | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    loadConfig()
  }, [])

  const loadConfig = async () => {
    setLoading(true)
    try {
      const data = await getAIConfig()
      setConfig(data)
      setBaseUrl(data.base_url)
      setModel(data.model)
    } catch {
      setMessage({ type: 'error', text: 'Error al cargar la configuracion' })
    } finally {
      setLoading(false)
    }
  }

  const handleSave = async () => {
    setSaving(true)
    setMessage(null)
    try {
      const updateData: Record<string, string> = {}
      if (apiKey) updateData.api_key = apiKey
      if (baseUrl) updateData.base_url = baseUrl
      if (model) updateData.model = model

      const updated = await updateAIConfig(updateData)
      setConfig(updated)
      setApiKey('')
      setMessage({ type: 'success', text: 'Configuracion guardada exitosamente' })
    } catch {
      setMessage({ type: 'error', text: 'Error al guardar la configuracion' })
    } finally {
      setSaving(false)
    }
  }

  if (loading) {
    return (
      <div className="card">
        <div className="flex items-center gap-2 mb-4">
          <Settings className="w-5 h-5 text-blue-600" />
          <h3 className="text-sm font-semibold text-slate-700">Configuracion de IA</h3>
        </div>
        <p className="text-sm text-slate-400">Cargando...</p>
      </div>
    )
  }

  return (
    <div className="card">
      <div className="flex items-center gap-2 mb-4">
        <Settings className="w-5 h-5 text-blue-600" />
        <h3 className="text-sm font-semibold text-slate-700">Configuracion de IA</h3>
      </div>

      {/* Status indicator */}
      <div className={`flex items-center gap-2 mb-4 p-2 rounded-lg text-xs ${
        config?.is_configured
          ? 'bg-green-50 text-green-700'
          : 'bg-amber-50 text-amber-700'
      }`}>
        {config?.is_configured ? (
          <>
            <Check className="w-3.5 h-3.5" />
            <span>API Key configurada: {config.api_key_masked}</span>
          </>
        ) : (
          <>
            <AlertCircle className="w-3.5 h-3.5" />
            <span>API Key no configurada. Ingresa tu clave para habilitar las funciones de IA.</span>
          </>
        )}
      </div>

      {/* API Key field */}
      <div className="mb-3">
        <label className="block text-xs font-medium text-slate-600 mb-1">
          API Key
        </label>
        <div className="relative">
          <input
            type={showKey ? 'text' : 'password'}
            value={apiKey}
            onChange={(e) => setApiKey(e.target.value)}
            placeholder={config?.is_configured ? 'Dejar vacio para mantener la actual' : 'Ingresa tu API key'}
            className="input-field w-full pr-10"
          />
          <button
            type="button"
            onClick={() => setShowKey(!showKey)}
            className="absolute right-2 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600"
          >
            {showKey ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
          </button>
        </div>
      </div>

      {/* Base URL field */}
      <div className="mb-3">
        <label className="block text-xs font-medium text-slate-600 mb-1">
          Base URL
        </label>
        <input
          type="text"
          value={baseUrl}
          onChange={(e) => setBaseUrl(e.target.value)}
          placeholder="https://integrate.api.nvidia.com/v1"
          className="input-field w-full"
        />
      </div>

      {/* Model field */}
      <div className="mb-4">
        <label className="block text-xs font-medium text-slate-600 mb-1">
          Modelo
        </label>
        <input
          type="text"
          value={model}
          onChange={(e) => setModel(e.target.value)}
          placeholder="meta/llama-3.1-405b-instruct"
          className="input-field w-full"
        />
      </div>

      {/* Save button */}
      <button
        onClick={handleSave}
        disabled={saving || (!apiKey && !baseUrl && !model)}
        className="btn-primary w-full text-sm disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {saving ? 'Guardando...' : 'Guardar Configuracion'}
      </button>

      {/* Message */}
      {message && (
        <p className={`mt-3 text-xs ${
          message.type === 'success' ? 'text-green-600' : 'text-red-600'
        }`}>
          {message.text}
        </p>
      )}
    </div>
  )
}
