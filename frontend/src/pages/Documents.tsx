import { useParams, Link } from 'react-router-dom'
import { ArrowLeft } from 'lucide-react'
import DocumentDownload from '../components/DocumentDownload'
import { PHASES } from '../types/research'

export default function Documents() {
  const { id } = useParams<{ id: string }>()

  const chapters = PHASES.map((phase) => ({
    id: phase.id,
    name: phase.name,
    available: false,
  }))

  return (
    <div className="max-w-4xl mx-auto px-6 py-8">
      <div className="flex items-center gap-4 mb-8">
        <Link
          to={`/project/${id}`}
          className="flex items-center gap-1 text-sm text-slate-600 hover:text-blue-600 transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          Volver al proyecto
        </Link>
      </div>

      <h1 className="text-2xl font-bold text-slate-900 mb-2">Documentos del Proyecto</h1>
      <p className="text-sm text-slate-500 mb-6">
        Genera y descarga documentos en formato APA 7 para cada capitulo de tu investigacion
      </p>

      <DocumentDownload projectId={id!} chapters={chapters} />
    </div>
  )
}
