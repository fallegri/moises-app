import { useCallback } from 'react'
import { useDropzone } from 'react-dropzone'
import { Upload, FileText, X } from 'lucide-react'
import { useState } from 'react'

interface FileUploadProps {
  onFilesAccepted: (files: File[]) => void
  disabled?: boolean
}

const ACCEPTED_TYPES = {
  'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'],
  'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ['.xlsx'],
  'text/markdown': ['.md'],
}

export default function FileUpload({ onFilesAccepted, disabled = false }: FileUploadProps) {
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
      <label className="block text-sm font-medium text-slate-700 mb-2">
        Subir archivos
      </label>
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
