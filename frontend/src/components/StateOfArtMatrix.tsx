import { useState } from 'react'
import { Plus, Trash2, Loader2 } from 'lucide-react'
import { addStudy, setNoMoreStudies } from '../api/client'
import type { StudyEntry } from '../types/research'

interface StateOfArtMatrixProps {
  projectId: string
}

export default function StateOfArtMatrix({ projectId }: StateOfArtMatrixProps) {
  const [studies, setStudies] = useState<StudyEntry[]>([])
  const [noMoreResearch, setNoMoreResearch] = useState(false)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const addEmptyStudy = () => {
    const newStudy: StudyEntry = {
      id: crypto.randomUUID(),
      author: '',
      year: '',
      title: '',
      methodology: '',
      findings: '',
      relevance: '',
    }
    setStudies((prev) => [...prev, newStudy])
  }

  const updateStudy = (id: string, field: keyof StudyEntry, value: string) => {
    setStudies((prev) =>
      prev.map((s) => (s.id === id ? { ...s, [field]: value } : s))
    )
  }

  const removeStudy = (id: string) => {
    setStudies((prev) => prev.filter((s) => s.id !== id))
  }

  const handleSaveStudy = async (study: StudyEntry) => {
    if (!study.title.trim() || !study.author.trim()) {
      setError('El titulo y autor son requeridos para guardar un estudio')
      return
    }
    setSaving(true)
    setError(null)
    try {
      await addStudy(projectId, {
        title: study.title,
        authors: study.author,
        year: parseInt(study.year) || new Date().getFullYear(),
        methodology: study.methodology,
        findings: study.findings,
        relevance: study.relevance,
      })
    } catch (err: unknown) {
      const message = err instanceof Error ? err.message : 'Error al guardar el estudio'
      setError(message)
    } finally {
      setSaving(false)
    }
  }

  const handleNoMoreResearch = async (checked: boolean) => {
    setNoMoreResearch(checked)
    setError(null)
    try {
      await setNoMoreStudies(projectId, checked)
    } catch (err: unknown) {
      const message = err instanceof Error ? err.message : 'Error al actualizar'
      setError(message)
      setNoMoreResearch(!checked)
    }
  }

  const studiesNeeded = 6 - studies.length

  return (
    <div className="card">
      <div className="flex items-center justify-between mb-4">
        <div>
          <h3 className="text-sm font-semibold text-slate-700">
            Matriz de Estado de la Cuestion
          </h3>
          <p className="text-xs text-slate-500 mt-0.5">
            Agrega al menos 6 investigaciones similares a tu problema
          </p>
        </div>
        <button onClick={addEmptyStudy} className="btn-secondary flex items-center gap-1 text-sm">
          <Plus className="w-4 h-4" />
          Agregar
        </button>
      </div>

      {error && (
        <div className="mb-4 p-2 bg-red-50 border border-red-200 rounded text-xs text-red-600">
          {error}
        </div>
      )}

      {studies.length > 0 && (
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b border-slate-200">
                <th className="text-left py-2 px-2 font-medium text-slate-600">Autor</th>
                <th className="text-left py-2 px-2 font-medium text-slate-600">Ano</th>
                <th className="text-left py-2 px-2 font-medium text-slate-600">Titulo</th>
                <th className="text-left py-2 px-2 font-medium text-slate-600">Metodologia</th>
                <th className="text-left py-2 px-2 font-medium text-slate-600">Hallazgos</th>
                <th className="text-left py-2 px-2 font-medium text-slate-600">Relevancia</th>
                <th className="w-20"></th>
              </tr>
            </thead>
            <tbody>
              {studies.map((study) => (
                <tr key={study.id} className="border-b border-slate-100">
                  <td className="py-2 px-2">
                    <input
                      type="text"
                      value={study.author}
                      onChange={(e) => updateStudy(study.id, 'author', e.target.value)}
                      className="input-field text-xs"
                      placeholder="Autor"
                    />
                  </td>
                  <td className="py-2 px-2">
                    <input
                      type="text"
                      value={study.year}
                      onChange={(e) => updateStudy(study.id, 'year', e.target.value)}
                      className="input-field text-xs w-16"
                      placeholder="2024"
                    />
                  </td>
                  <td className="py-2 px-2">
                    <input
                      type="text"
                      value={study.title}
                      onChange={(e) => updateStudy(study.id, 'title', e.target.value)}
                      className="input-field text-xs"
                      placeholder="Titulo"
                    />
                  </td>
                  <td className="py-2 px-2">
                    <input
                      type="text"
                      value={study.methodology}
                      onChange={(e) => updateStudy(study.id, 'methodology', e.target.value)}
                      className="input-field text-xs"
                      placeholder="Metodologia"
                    />
                  </td>
                  <td className="py-2 px-2">
                    <input
                      type="text"
                      value={study.findings}
                      onChange={(e) => updateStudy(study.id, 'findings', e.target.value)}
                      className="input-field text-xs"
                      placeholder="Hallazgos"
                    />
                  </td>
                  <td className="py-2 px-2">
                    <input
                      type="text"
                      value={study.relevance}
                      onChange={(e) => updateStudy(study.id, 'relevance', e.target.value)}
                      className="input-field text-xs"
                      placeholder="Relevancia"
                    />
                  </td>
                  <td className="py-2 px-2 flex gap-1">
                    <button
                      onClick={() => handleSaveStudy(study)}
                      disabled={saving}
                      className="text-slate-400 hover:text-blue-500 transition-colors text-xs px-1"
                      title="Guardar estudio"
                    >
                      {saving ? <Loader2 className="w-4 h-4 animate-spin" /> : '✓'}
                    </button>
                    <button
                      onClick={() => removeStudy(study.id)}
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

      {studies.length === 0 && (
        <div className="text-center py-8 text-slate-400">
          <p className="text-sm">No hay investigaciones agregadas aun</p>
          <p className="text-xs mt-1">Haz clic en &quot;Agregar&quot; para comenzar</p>
        </div>
      )}

      {studiesNeeded > 0 && studies.length > 0 && !noMoreResearch && (
        <p className="text-xs text-amber-600 mt-3">
          Necesitas agregar {studiesNeeded} investigacion{studiesNeeded > 1 ? 'es' : ''} mas
        </p>
      )}

      <div className="mt-4 pt-4 border-t border-slate-200">
        <label className="flex items-center gap-2 cursor-pointer">
          <input
            type="checkbox"
            checked={noMoreResearch}
            onChange={(e) => handleNoMoreResearch(e.target.checked)}
            className="rounded border-slate-300 text-blue-600 focus:ring-blue-500"
          />
          <span className="text-sm text-slate-700">
            No se encontraron mas investigaciones similares
          </span>
        </label>
      </div>
    </div>
  )
}
