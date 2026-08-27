import { useCallback, useState } from 'react'
import { useDropzone } from 'react-dropzone'
import { Upload, FileText, X } from 'lucide-react'

interface FileUploadProps {
  onFilesAccepted: (files: File[]) => void
  disabled?: boolean
  /** Optional phase-specific note about what the file is for. */
  purpose?: string
}

// Standardized note making clear the upload is optional and what formats are
// accepted, consistent with the backend wording.
const OPTIONAL_NOTE =
  'Opcional: adjunta documentos de respaldo (.docx, .xlsx, .md). No es necesario subir archivos para continuar.'

const ACCEPTED_TYPES = {
  'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'],
  'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ['.xlsx'],
  'text/markdown': ['.md'],
}

export default function FileUpload({
  onFilesAccepted,
  disabled = false,
  purpose,
}: FileUploadProps) {
  const [stagedFiles, setStagedFiles] = useState<File[]>([])

  const onDrop = useCallback((acceptedFiles: File[]) => {
    setStagedFiles((prev) => [...prev, ...acceptedFiles])
  }, [])

  const removeFile = (index: number) => {
    setStagedFiles((prev) => prev.filter((_, i) => i !== index))
  }

  const handleUpload = () => {
    if (stagedFiles.length > 0) {
      onFilesAccepted(stagedFiles)
      setStagedFiles([])
    }
  }

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: ACCEPTED_TYPES,
    disabled,
  })

  return (
    <div className="card">
      <label className="block text-sm font-medium text-slate-700 mb-1">
        Subir archivos
      </label>
      <p className="text-xs font-medium text-slate-600">{OPTIONAL_NOTE}</p>
      {purpose && <p className="text-xs text-slate-500 mt-1 mb-3">{purpose}</p>}
      {!purpose && <div className="mb-3" />}
      <div
        {...getRootProps()}
        className={`border-2 border-dashed rounded-lg p-6 text-center cursor-pointer transition-colors ${
          isDragActive
            ? 'border-blue-400 bg-blue-50'
            : 'border-slate-300 hover:border-blue-300 hover:bg-slate-50'
        } ${disabled ? 'opacity-50 cursor-not-allowed' : ''}`}
      >
        <input {...getInputProps()} />
        <Upload className="w-8 h-8 text-slate-400 mx-auto mb-2" />
        {isDragActive ? (
          <p className="text-sm text-blue-600">Suelta los archivos aqui...</p>
        ) : (
          <div>
            <p className="text-sm text-slate-600">
              Arrastra archivos aqui o haz clic para seleccionar
            </p>
            <p className="text-xs text-slate-400 mt-1">
              Formatos aceptados: .docx, .xlsx, .md
            </p>
          </div>
        )}
      </div>

      {stagedFiles.length > 0 && (
        <div className="mt-3 space-y-2">
          {stagedFiles.map((file, index) => (
            <div
              key={`${file.name}-${index}`}
              className="flex items-center justify-between bg-slate-50 rounded-lg px-3 py-2"
            >
              <div className="flex items-center gap-2">
                <FileText className="w-4 h-4 text-blue-600" />
                <span className="text-sm text-slate-700">{file.name}</span>
                <span className="text-xs text-slate-400">
                  ({(file.size / 1024).toFixed(1)} KB)
                </span>
              </div>
              <button
                onClick={() => removeFile(index)}
                className="text-slate-400 hover:text-red-500 transition-colors"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
          ))}
          <button
            onClick={handleUpload}
            disabled={disabled}
            className="btn-primary text-sm w-full mt-2"
          >
            Subir {stagedFiles.length} archivo{stagedFiles.length > 1 ? 's' : ''}
          </button>
        </div>
      )}
    </div>
  )
}
