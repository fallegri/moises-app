import { useState } from 'react'
import { CheckCircle2 } from 'lucide-react'

interface OptionSelectorProps {
  options: string[]
  onSelect: (index: number) => void
  disabled?: boolean
}

export default function OptionSelector({ options, onSelect, disabled = false }: OptionSelectorProps) {
  const [selectedIndex, setSelectedIndex] = useState<number | null>(null)

  const handleConfirm = () => {
    if (selectedIndex !== null) {
      onSelect(selectedIndex)
    }
  }

  return (
    <div className="card">
      <h3 className="text-sm font-semibold text-slate-700 mb-3">
        Selecciona una opcion
      </h3>
      <div className="space-y-3">
        {options.map((option, index) => (
          <button
            key={index}
            onClick={() => setSelectedIndex(index)}
            disabled={disabled}
            className={`w-full text-left p-4 rounded-lg border-2 transition-all ${
              selectedIndex === index
                ? 'border-blue-500 bg-blue-50 ring-1 ring-blue-200'
                : 'border-slate-200 hover:border-slate-300 hover:bg-slate-50'
            } ${disabled ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer'}`}
          >
            <div className="flex items-start gap-3">
              <div className="flex-shrink-0 mt-0.5">
                {selectedIndex === index ? (
                  <CheckCircle2 className="w-5 h-5 text-blue-600" />
                ) : (
                  <div className="w-5 h-5 rounded-full border-2 border-slate-300" />
                )}
              </div>
              <div className="flex-1">
                <p className="text-sm font-medium text-slate-800 mb-1">
                  Opcion {index + 1}
                </p>
                <p className="text-sm text-slate-600">{option}</p>
              </div>
            </div>
          </button>
        ))}
      </div>
      <button
        onClick={handleConfirm}
        disabled={disabled || selectedIndex === null}
        className="btn-primary mt-4 w-full"
      >
        Confirmar seleccion
      </button>
    </div>
  )
}
