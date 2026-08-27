import { useEffect, useState } from 'react'
import { Search, Upload, BookOpen, FileText } from 'lucide-react'
import { searchKnowledge, uploadKnowledge, getKnowledgeDocuments } from '../api/client'
import type { KnowledgeSearchResult } from '../types/research'

export default function KnowledgeBase() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<KnowledgeSearchResult[]>([])
  const [searching, setSearching] = useState(false)
  const [uploading, setUploading] = useState(false)
  const [uploadMessage, setUploadMessage] = useState('')
  const [documents, setDocuments] = useState<string[]>([])

  const loadDocuments = async () => {
    try {
      const data = await getKnowledgeDocuments()
      setDocuments(data.documents)
    } catch {
      // Ignore errors loading the document list
    }
  }

  useEffect(() => {
    loadDocuments()
  }, [])

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
    const files = e.target.files
    if (!files || files.length === 0) return
    setUploading(true)
    setUploadMessage('')
    try {
      let uploaded = 0
      for (const file of Array.from(files)) {
        await uploadKnowledge(file)
        uploaded++
      }
      setUploadMessage(
        uploaded === 1
          ? 'Archivo subido exitosamente'
          : `${uploaded} archivos subidos exitosamente`
      )
      await loadDocuments()
    } catch {
      setUploadMessage('Error al subir el archivo')
    } finally {
      setUploading(false)
      // Reset the input so selecting the same files again re-triggers onChange
      e.target.value = ''
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
            multiple
          />
        </label>
        {uploading && <span className="text-xs text-slate-400">Subiendo...</span>}
        {uploadMessage && (
          <span className="text-xs text-green-600">{uploadMessage}</span>
        )}
      </div>

      {/* Uploaded documents list */}
      <div className="mb-4">
        <h4 className="text-xs font-semibold text-slate-500 uppercase mb-2">
          Documentos cargados ({documents.length})
        </h4>
        {documents.length > 0 ? (
          <ul className="space-y-1">
            {documents.map((doc) => (
              <li
                key={doc}
                className="flex items-center gap-2 text-sm text-slate-600 p-2 bg-slate-50 rounded-lg"
              >
                <FileText className="w-4 h-4 text-slate-400 flex-shrink-0" />
                <span className="truncate">{doc}</span>
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-xs text-slate-400">Aun no se han cargado documentos.</p>
        )}
      </div>

      {/* Results */}
      {results.length > 0 && (
        <div className="space-y-3">
          <h4 className="text-xs font-semibold text-slate-500 uppercase">
            Resultados ({results.length})
          </h4>
          {results.map((result, index) => (
            <div key={`${result.filename}-${index}`} className="p-3 bg-slate-50 rounded-lg">
              <h5 className="text-sm font-medium text-slate-800">{result.heading}</h5>
              <p className="text-xs text-slate-400 mt-0.5">{result.filename} (score: {result.score})</p>
              <p className="text-xs text-slate-500 mt-1 line-clamp-3">
                {result.content}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
