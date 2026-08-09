import { useState } from 'react'
import { Send } from 'lucide-react'

interface TextInputProps {
  onSubmit: (text: string) => void
  disabled?: boolean
  placeholder?: string
}

export default function TextInput({
  onSubmit,
  disabled = false,
  placeholder = 'Escribe aqui tu informacion, antecedentes, respuestas a las tareas...',
}: TextInputProps) {
  const [text, setText] = useState('')

  const handleSubmit = () => {
    if (text.trim()) {
      onSubmit(text.trim())
      setText('')
    }
  }

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && e.ctrlKey) {
      handleSubmit()
    }
  }

  return (
    <div className="card">
      <label className="block text-sm font-medium text-slate-700 mb-2">
        Tu respuesta
      </label>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={handleKeyDown}
        disabled={disabled}
        placeholder={placeholder}
        rows={6}
        className="input-field resize-y min-h-[120px]"
      />
      <div className="flex items-center justify-between mt-3">
        <p className="text-xs text-slate-400">Ctrl+Enter para enviar</p>
        <button
          onClick={handleSubmit}
          disabled={disabled || !text.trim()}
          className="btn-primary flex items-center gap-2 text-sm"
        >
          <Send className="w-4 h-4" />
          Enviar
        </button>
      </div>
    </div>
  )
}
