import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Plus, BookOpen, Trash2, ArrowRight, Loader2 } from 'lucide-react'
import { useProjects, useCreateProject, useDeleteProject } from '../hooks/useWorkflow'

export default function Home() {
  const navigate = useNavigate()
  const { data: projects, isLoading } = useProjects()
  const createProject = useCreateProject()
  const deleteProject = useDeleteProject()
  const [showForm, setShowForm] = useState(false)
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')

  const handleCreate = async () => {
    if (!title.trim()) return
    const project = await createProject.mutateAsync({
      title: title.trim(),
      description: description.trim(),
    })
    setTitle('')
    setDescription('')
    setShowForm(false)
    navigate(`/project/${project.id}`)
  }

  const handleDelete = (id: string, e: React.MouseEvent) => {
    e.stopPropagation()
    if (confirm('Estas seguro de eliminar este proyecto?')) {
      deleteProject.mutate(id)
    }
  }

  return (
    <div className="max-w-5xl mx-auto px-6 py-10">
      {/* Hero Section */}
      <div className="text-center mb-12">
        <div className="inline-flex items-center justify-center w-16 h-16 bg-blue-100 rounded-2xl mb-4">
          <BookOpen className="w-8 h-8 text-blue-600" />
        </div>
        <h1 className="text-3xl font-bold text-slate-900 mb-3">
          Asistente de Investigacion Cientifica
        </h1>
        <p className="text-lg text-slate-600 max-w-2xl mx-auto">
          Te guio paso a paso a traves del proceso de investigacion cientifica, desde la
          identificacion del problema hasta el marco metodologico. Cada capitulo se genera en formato APA 7.
        </p>
      </div>

      {/* Features */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-12">
        <div className="card text-center">
          <div className="text-2xl mb-2">🔍</div>
          <h3 className="text-sm font-semibold text-slate-800">Identificacion del Problema</h3>
          <p className="text-xs text-slate-500 mt-1">
            Analizo tu situacion problematica y te ayudo a formular el problema de investigacion
          </p>
        </div>
        <div className="card text-center">
          <div className="text-2xl mb-2">📚</div>
          <h3 className="text-sm font-semibold text-slate-800">Guia Paso a Paso</h3>
          <p className="text-xs text-slate-500 mt-1">
            12 fases del metodo cientifico con validacion de coherencia en cada etapa
          </p>
        </div>
        <div className="card text-center">
          <div className="text-2xl mb-2">📄</div>
          <h3 className="text-sm font-semibold text-slate-800">Documentos APA 7</h3>
          <p className="text-xs text-slate-500 mt-1">
            Genera automaticamente capitulos formateados segun las normas APA 7ma edicion
          </p>
        </div>
      </div>

      {/* Projects Section */}
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-xl font-bold text-slate-900">Mis Proyectos</h2>
        <button
          onClick={() => setShowForm(true)}
          className="btn-primary flex items-center gap-2"
        >
          <Plus className="w-4 h-4" />
          Nuevo Proyecto
        </button>
      </div>

      {/* Create Project Form */}
      {showForm && (
        <div className="card mb-6">
          <h3 className="text-sm font-semibold text-slate-700 mb-3">Crear Nuevo Proyecto</h3>
          <div className="space-y-3">
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Titulo del proyecto de investigacion"
              className="input-field"
              autoFocus
            />
            <textarea
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              placeholder="Descripcion breve (opcional)"
              className="input-field resize-none"
              rows={3}
            />
            <div className="flex gap-2 justify-end">
              <button
                onClick={() => setShowForm(false)}
                className="btn-secondary text-sm"
              >
                Cancelar
              </button>
              <button
                onClick={handleCreate}
                disabled={!title.trim() || createProject.isPending}
                className="btn-primary text-sm flex items-center gap-2"
              >
                {createProject.isPending && <Loader2 className="w-4 h-4 animate-spin" />}
                Crear Proyecto
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Projects List */}
      {isLoading ? (
        <div className="text-center py-12">
          <Loader2 className="w-6 h-6 animate-spin text-blue-600 mx-auto" />
          <p className="text-sm text-slate-500 mt-2">Cargando proyectos...</p>
        </div>
      ) : projects && projects.length > 0 ? (
        <div className="space-y-3">
          {projects.map((project) => (
            <div
              key={project.id}
              onClick={() => navigate(`/project/${project.id}`)}
              className="card cursor-pointer hover:shadow-md transition-shadow flex items-center justify-between group"
            >
              <div className="flex-1 min-w-0">
                <h3 className="text-sm font-semibold text-slate-800 truncate">
                  {project.title}
                </h3>
                {project.description && (
                  <p className="text-xs text-slate-500 mt-0.5 truncate">
                    {project.description}
                  </p>
                )}
                <div className="flex items-center gap-3 mt-2">
                  <div className="flex-1 max-w-[200px] h-1.5 bg-slate-200 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-blue-500 rounded-full"
                      style={{ width: `${project.progress}%` }}
                    />
                  </div>
                  <span className="text-xs text-slate-400">{project.progress}%</span>
                </div>
              </div>
              <div className="flex items-center gap-2 ml-4">
                <button
                  onClick={(e) => handleDelete(project.id, e)}
                  className="opacity-0 group-hover:opacity-100 text-slate-400 hover:text-red-500 transition-all p-1"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
                <ArrowRight className="w-5 h-5 text-slate-400 group-hover:text-blue-600 transition-colors" />
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className="text-center py-12 card">
          <BookOpen className="w-10 h-10 text-slate-300 mx-auto mb-3" />
          <h3 className="text-sm font-medium text-slate-600">No tienes proyectos aun</h3>
          <p className="text-xs text-slate-400 mt-1">
            Crea tu primer proyecto de investigacion para comenzar
          </p>
        </div>
      )}
    </div>
  )
}
