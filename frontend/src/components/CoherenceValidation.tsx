import { CheckCircle2, XCircle, AlertTriangle } from 'lucide-react'
import type { ValidationResult } from '../types/research'

interface CoherenceValidationProps {
  result: ValidationResult
}

export default function CoherenceValidation({ result }: CoherenceValidationProps) {
  return (
    <div className={`card border-l-4 ${result.is_valid ? 'border-l-green-500' : 'border-l-amber-500'}`}>
      <div className="flex items-center gap-2 mb-3">
        {result.is_valid ? (
          <CheckCircle2 className="w-5 h-5 text-green-600" />
        ) : (
          <AlertTriangle className="w-5 h-5 text-amber-600" />
        )}
        <h3 className="text-sm font-semibold text-slate-700">
          Validacion de Coherencia
        </h3>
        <span className={`text-xs px-2 py-0.5 rounded-full ${
          result.is_valid
            ? 'bg-green-100 text-green-700'
            : 'bg-amber-100 text-amber-700'
        }`}>
          {result.is_valid ? 'Aprobado' : 'Necesita revision'}
        </span>
      </div>

      <div className="mb-3">
        <div className="flex items-center gap-2">
          <div className="flex-1 h-2 bg-slate-200 rounded-full overflow-hidden">
            <div
              className={`h-full rounded-full ${
                result.score >= 80
                  ? 'bg-green-500'
                  : result.score >= 60
                  ? 'bg-amber-500'
                  : 'bg-red-500'
              }`}
              style={{ width: `${result.score}%` }}
            />
          </div>
          <span className="text-xs font-medium text-slate-600">{result.score}%</span>
        </div>
      </div>

      {result.message && (
        <div className="mb-3">
          <p className="text-xs text-slate-600">{result.message}</p>
        </div>
      )}

      {result.issues && result.issues.length > 0 && (
        <div className="mb-3">
          <h4 className="text-xs font-semibold text-red-700 mb-1">Problemas encontrados:</h4>
          <ul className="space-y-1">
            {result.issues.map((issue, i) => (
              <li key={i} className="flex items-start gap-2 text-xs text-red-600">
                <XCircle className="w-3 h-3 mt-0.5 flex-shrink-0" />
                {issue}
              </li>
            ))}
          </ul>
        </div>
      )}

      {result.suggestions && result.suggestions.length > 0 && (
        <div>
          <h4 className="text-xs font-semibold text-blue-700 mb-1">Sugerencias:</h4>
          <ul className="space-y-1">
            {result.suggestions.map((suggestion, i) => (
              <li key={i} className="flex items-start gap-2 text-xs text-blue-600">
                <span className="text-blue-400 mt-0.5">-</span>
                {suggestion}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  )
}
