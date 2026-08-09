import { useState } from 'react'
import { Download, FileText, Loader2 } from 'lucide-react'
import { generateDocument, getDocumentDownloadUrl } from '../api/client'

interface DocumentDownloadProps {
  projectId: string
  chapters: { id: string; name: string; available: boolean }[]
}

export default function DocumentDownload({ projectId, chapters }: DocumentDownloadProps) {
  const [generating, setGenerating] = useState<string | null>(null)

  const handleGenerate = async (chapter: string) => {
    setGenerating(chapter)
    try {
      await generateDocument(projectId, chapter)
    } finally {
      setGenerating(null)
    }
  }

  const handleDownload = (chapter: string) => {
    const url = getDocumentDownloadUrl(projectId, chapter)
    window.open(url, '_blank')
  }

  return (
    <div className="card">
      <h3 className="text-sm font-semibold text-slate-700 mb-4">
        Documentos Generados (Formato APA 7)
      </h3>
      <div className="space-y-3">
        {chapters.map((chapter) => (
          <div
            key={chapter.id}
            className="flex items-center justify-between p-3 bg-slate-50 rounded-lg"
          >
            <div className="flex items-center gap-3">
              <FileText className="w-5 h-5 text-blue-600" />
              <span className="text-sm font-medium text-slate-700">{chapter.name}</span>
            </div>
            <div className="flex items-center gap-2">
              <button
                onClick={() => handleGenerate(chapter.id)}
                disabled={generating === chapter.id}
                className="btn-secondary text-xs flex items-center gap-1"
              >
                {generating === chapter.id ? (
                  <Loader2 className="w-3 h-3 animate-spin" />
                ) : (
                  <FileText className="w-3 h-3" />
                )}
                Generar
              </button>
              {chapter.available && (
                <button
                  onClick={() => handleDownload(chapter.id)}
                  className="btn-primary text-xs flex items-center gap-1"
                >
                  <Download className="w-3 h-3" />
                  Descargar
                </button>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
