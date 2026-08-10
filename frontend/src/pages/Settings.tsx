import AIConfig from '../components/AIConfig'

export default function SettingsPage() {
  return (
    <div className="max-w-2xl mx-auto px-6 py-8">
      <h1 className="text-2xl font-bold text-slate-900 mb-2">Configuracion</h1>
      <p className="text-sm text-slate-500 mb-6">
        Administra la configuracion del asistente de investigacion.
      </p>
      <AIConfig />
    </div>
  )
}
