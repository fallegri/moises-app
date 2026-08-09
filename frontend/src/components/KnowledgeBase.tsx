import { useState } from 'react'
import { Search, Upload, BookOpen } from 'lucide-react'
import { searchKnowledge, uploadKnowledge } from '../api/client'
import type { KnowledgeDocument } from '../types/research'

export default function KnowledgeBase() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<KnowledgeDocument[]>([])
  const [searching, setSearching] = useState(false)
  const [uploading, setUploading] = useState(false)
  const [uploadMessage, setUploadMessage] = useState('')

  const handleSearch = async () => {
    if (!query.trim()) return
    setSearching(true)
    try {
      const data = await searchKnowledge(query)
      setResults(data)
    } finally {
      setSearching(false)
    }
  }

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return
    setUploading(true)
    setUploadMessage('')
    try {
      const result = await uploadKnowledge(file)
      setUploadMessage(result.message || 'Archivo subido exitosamente')
    } catch {
      setUploadMessage('Error al subir el archivo')
    } finally {
      setUploading(false)
    }
  }

  return (
    <div className="card">
      <div className="flex items-center gap-2 mb-4">
        <BookOpen className="w-5 h-5 text-blue-600" />
        <h3 className="text-sm font-semibold text-slate-700">Base de Conocimiento</h3>
      </div>

      {/* Search */}
      <div className="flex gap-2 mb-4">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
          placeholder="Buscar en la base de conocimiento..."
          className="input-field flex-1"
        />
        <button
          onClick={handleSearch}
          disabled={searching}
          className="btn-primary flex items-center gap-1 text-sm"
        >
          <Search className="w-4 h-4" />
          Buscar
        </button>
      </div>

      {/* Upload */}
      <div className="flex items-center gap-3 mb-4 p-3 bg-slate-50 rounded-lg">
        <Upload className="w-4 h-4 text-slate-500" />
        <label className="text-sm text-slate-600 cursor-pointer hover:text-blue-600">
          Subir literatura adicional
          <input
            type="file"
            className="hidden"
            onChange={handleUpload}
            disabled={uploading}
            accept=".md,.docx,.xlsx"
          />
        </label>
        {uploading && <span className="text-xs text-slate-400">Subiendo...</span>}
        {uploadMessage && (
          <span className="text-xs text-green-600">{uploadMessage}</span>
        )}
      </div>

      {/* Results */}
      {results.length > 0 && (
        <div className="space-y-3">
          <h4 className="text-xs font-semibold text-slate-500 uppercase">
            Resultados ({results.length})
          </h4>
          {results.map((doc) => (
            <div key={doc.id} className="p-3 bg-slate-50 rounded-lg">
              <h5 className="text-sm font-medium text-slate-800">{doc.title}</h5>
              <p className="text-xs text-slate-500 mt-1 line-clamp-3">
                {doc.content_preview}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
