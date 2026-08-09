import ReactMarkdown from 'react-markdown'
import { Bot } from 'lucide-react'

interface AIResponseProps {
  content: string
}

export default function AIResponse({ content }: AIResponseProps) {
  return (
    <div className="card border-l-4 border-l-blue-500">
      <div className="flex items-center gap-2 mb-3">
        <Bot className="w-5 h-5 text-blue-600" />
        <h3 className="text-sm font-semibold text-blue-900">Respuesta del Asistente</h3>
      </div>
      <div className="prose prose-sm prose-slate max-w-none">
        <ReactMarkdown>{content}</ReactMarkdown>
      </div>
    </div>
  )
}
