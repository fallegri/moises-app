import { useState } from 'react'
import { Plus, Trash2 } from 'lucide-react'
import type { VariableEntry } from '../types/research'

export default function VariableMatrix() {
  const [variables, setVariables] = useState<VariableEntry[]>([])

  const addVariable = () => {
    const newVar: VariableEntry = {
      id: crypto.randomUUID(),
      variable: '',
      dimensions: '',
      indicators: '',
      instruments: '',
    }
    setVariables((prev) => [...prev, newVar])
  }

  const updateVariable = (id: string, field: keyof VariableEntry, value: string) => {
    setVariables((prev) =>
      prev.map((v) => (v.id === id ? { ...v, [field]: value } : v))
    )
  }

  const removeVariable = (id: string) => {
    setVariables((prev) => prev.filter((v) => v.id !== id))
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
        <button onClick={addVariable} className="btn-secondary flex items-center gap-1 text-sm">
          <Plus className="w-4 h-4" />
          Agregar Variable
        </button>
      </div>

      {variables.length > 0 && (
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b border-slate-200">
                <th className="text-left py-2 px-2 font-medium text-slate-600">Variable</th>
                <th className="text-left py-2 px-2 font-medium text-slate-600">Dimensiones</th>
                <th className="text-left py-2 px-2 font-medium text-slate-600">Indicadores</th>
                <th className="text-left py-2 px-2 font-medium text-slate-600">Instrumentos</th>
                <th className="w-10"></th>
              </tr>
            </thead>
            <tbody>
              {variables.map((v) => (
                <tr key={v.id} className="border-b border-slate-100">
                  <td className="py-2 px-2">
                    <input
                      type="text"
                      value={v.variable}
                      onChange={(e) => updateVariable(v.id, 'variable', e.target.value)}
                      className="input-field text-xs"
                      placeholder="Nombre de variable"
                    />
                  </td>
                  <td className="py-2 px-2">
                    <input
                      type="text"
                      value={v.dimensions}
                      onChange={(e) => updateVariable(v.id, 'dimensions', e.target.value)}
                      className="input-field text-xs"
                      placeholder="Dimensiones"
                    />
                  </td>
                  <td className="py-2 px-2">
                    <input
                      type="text"
                      value={v.indicators}
                      onChange={(e) => updateVariable(v.id, 'indicators', e.target.value)}
                      className="input-field text-xs"
                      placeholder="Indicadores"
                    />
                  </td>
                  <td className="py-2 px-2">
                    <input
                      type="text"
                      value={v.instruments}
                      onChange={(e) => updateVariable(v.id, 'instruments', e.target.value)}
                      className="input-field text-xs"
                      placeholder="Instrumentos"
                    />
                  </td>
                  <td className="py-2 px-2">
                    <button
                      onClick={() => removeVariable(v.id)}
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

      {variables.length === 0 && (
        <div className="text-center py-8 text-slate-400">
          <p className="text-sm">No hay variables definidas aun</p>
          <p className="text-xs mt-1">Haz clic en &quot;Agregar Variable&quot; para comenzar</p>
        </div>
      )}
    </div>
  )
}
