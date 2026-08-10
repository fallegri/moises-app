import { useState, useEffect } from 'react'
import { Plus, Trash2, Loader2 } from 'lucide-react'
import { addVariable, removeVariable, listVariables } from '../api/client'
import type { VariableEntry } from '../types/research'

interface VariableMatrixProps {
  projectId: string
}

export default function VariableMatrix({ projectId }: VariableMatrixProps) {
  const [variables, setVariables] = useState<VariableEntry[]>([])
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [showForm, setShowForm] = useState(false)
  const [newVar, setNewVar] = useState({
    variable: '',
    dimensions: '',
    indicators: '',
    instruments: '',
  })

  useEffect(() => {
    loadVariables()
  }, [projectId])

  const loadVariables = async () => {
    try {
      setLoading(true)
      const result = await listVariables(projectId)
      setVariables(
        result.variables.map((v) => ({
          id: v.name,
          variable: v.name,
          dimensions: v.dimensions.join(', '),
          indicators: v.indicators.join(', '),
          instruments: v.type,
        }))
      )
    } catch {
      // If the endpoint fails (e.g., project not found), leave empty
    } finally {
      setLoading(false)
    }
  }

  const handleAdd = async () => {
    if (!newVar.variable.trim()) return
    setSaving(true)
    try {
      await addVariable(projectId, {
        name: newVar.variable.trim(),
        type: newVar.instruments.trim() || 'Sin especificar',
        conceptual_definition: newVar.dimensions.trim() || 'Sin definicion',
        operational_definition: newVar.indicators.trim() || 'Sin definicion',
        dimensions: newVar.dimensions ? newVar.dimensions.split(',').map((d) => d.trim()) : [],
        indicators: newVar.indicators ? newVar.indicators.split(',').map((i) => i.trim()) : [],
      })
      setNewVar({ variable: '', dimensions: '', indicators: '', instruments: '' })
      setShowForm(false)
      await loadVariables()
    } catch {
      // Handle error silently for now
    } finally {
      setSaving(false)
    }
  }

  const handleRemove = async (name: string) => {
    try {
      await removeVariable(projectId, name)
      await loadVariables()
    } catch {
      // Handle error silently
    }
  }

  if (loading) {
    return (
      <div className="card">
        <div className="flex items-center justify-center py-8">
          <Loader2 className="w-5 h-5 animate-spin text-blue-600" />
          <span className="text-sm text-slate-500 ml-2">Cargando variables...</span>
        </div>
      </div>
    )
  }

  return (
    <div className="card">
      <div className="flex items-center justify-between mb-4">
        <div>
          <h3 className="text-sm font-semibold text-slate-700">
            Matriz de Conceptualizacion de Variables
          </h3>
          <p className="text-xs text-slate-500 mt-0.5">
            Define las variables, dimensiones, indicadores e instrumentos
          </p>
        </div>
        <button
          onClick={() => setShowForm(true)}
          className="btn-secondary flex items-center gap-1 text-sm"
        >
          <Plus className="w-4 h-4" />
          Agregar Variable
        </button>
      </div>

      {showForm && (
        <div className="mb-4 p-3 bg-slate-50 rounded-lg space-y-2">
          <input
            type="text"
            value={newVar.variable}
            onChange={(e) => setNewVar({ ...newVar, variable: e.target.value })}
            className="input-field text-xs"
            placeholder="Nombre de variable"
          />
          <input
            type="text"
            value={newVar.dimensions}
            onChange={(e) => setNewVar({ ...newVar, dimensions: e.target.value })}
            className="input-field text-xs"
            placeholder="Dimensiones (separadas por coma)"
          />
          <input
            type="text"
            value={newVar.indicators}
            onChange={(e) => setNewVar({ ...newVar, indicators: e.target.value })}
            className="input-field text-xs"
            placeholder="Indicadores (separados por coma)"
          />
          <input
            type="text"
            value={newVar.instruments}
            onChange={(e) => setNewVar({ ...newVar, instruments: e.target.value })}
            className="input-field text-xs"
            placeholder="Tipo de variable (independiente, dependiente, interviniente)"
          />
          <div className="flex gap-2 justify-end">
            <button
              onClick={() => setShowForm(false)}
              className="btn-secondary text-xs"
            >
              Cancelar
            </button>
            <button
              onClick={handleAdd}
              disabled={!newVar.variable.trim() || saving}
              className="btn-primary text-xs flex items-center gap-1"
            >
              {saving && <Loader2 className="w-3 h-3 animate-spin" />}
              Guardar
            </button>
          </div>
        </div>
      )}

      {variables.length > 0 && (
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b border-slate-200">
                <th className="text-left py-2 px-2 font-medium text-slate-600">Variable</th>
                <th className="text-left py-2 px-2 font-medium text-slate-600">Dimensiones</th>
                <th className="text-left py-2 px-2 font-medium text-slate-600">Indicadores</th>
                <th className="text-left py-2 px-2 font-medium text-slate-600">Tipo</th>
                <th className="w-10"></th>
              </tr>
            </thead>
            <tbody>
              {variables.map((v) => (
                <tr key={v.id} className="border-b border-slate-100">
                  <td className="py-2 px-2 text-xs text-slate-700">{v.variable}</td>
                  <td className="py-2 px-2 text-xs text-slate-600">{v.dimensions}</td>
                  <td className="py-2 px-2 text-xs text-slate-600">{v.indicators}</td>
                  <td className="py-2 px-2 text-xs text-slate-600">{v.instruments}</td>
                  <td className="py-2 px-2">
                    <button
                      onClick={() => handleRemove(v.variable)}
                      className="text-slate-400 hover:text-red-500 transition-colors"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {variables.length === 0 && !showForm && (
        <div className="text-center py-8 text-slate-400">
          <p className="text-sm">No hay variables definidas aun</p>
          <p className="text-xs mt-1">Haz clic en &quot;Agregar Variable&quot; para comenzar</p>
        </div>
      )}
    </div>
  )
}
