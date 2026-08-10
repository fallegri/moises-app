# Asistente de Investigacion

Sistema inteligente de asistencia y guia para la investigacion cientifica. Guia al usuario paso a paso en el desarrollo de su proyecto de investigacion, desde la identificacion del problema hasta la generacion de documentos con formato APA 7.

## Descripcion

Este sistema acompana al investigador en todo el proceso de investigacion, utilizando inteligencia artificial para:

- Analizar la situacion problematica descrita por el usuario
- Identificar el problema de investigacion
- Sugerir instrumentos de recopilacion de datos
- Refinar el problema con 3 formulaciones basadas en el metodo cientifico
- Generar preguntas de investigacion
- Guiar la construccion de cada capitulo de la tesis
- Validar la coherencia en cada etapa
- Generar documentos en formato APA 7

El sistema utiliza como referencia una base de conocimiento con libros de metodologia de investigacion, incluyendo Sampieri, Vara-Horna, y el Manual APA 7.

## Arquitectura

```
┌─────────────┐       ┌─────────────────┐       ┌──────────────────┐
│   Frontend  │──────▶│    Backend API   │──────▶│  Proveedor IA    │
│  React+Vite │◀──────│  FastAPI/Python  │◀──────│ (NVIDIA/OpenAI)  │
└─────────────┘       └────────┬────────┘       └──────────────────┘
                               │
                    ┌──────────┴──────────┐
                    │  Base de Conocimiento │
                    │  (skills/knowledge/) │
                    └─────────────────────┘
```

- **Frontend**: React 19 + TypeScript + Vite + Tailwind CSS
- **Backend**: Python 3.11 + FastAPI + Uvicorn
- **IA**: Compatible con OpenAI API (NVIDIA NIM, Claude, Ollama, etc.)
- **Base de Conocimiento**: ~42 archivos Markdown con libros de metodologia

## Requisitos Previos

- Python 3.11+
- Node.js 22+
- Docker y Docker Compose (opcional, para despliegue)
- Clave API de un proveedor compatible con OpenAI (NVIDIA, OpenAI, Anthropic, Ollama)

## Configuracion Local (Desarrollo)

### 1. Clonar el repositorio

```bash
git clone https://github.com/fallegri/moises-app.git
cd moises-app
```

### 2. Configurar el Backend

```bash
cd backend

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con su clave API
```

### 3. Configurar el Frontend

```bash
cd frontend

# Instalar dependencias
npm install
```

### 4. Iniciar los servicios

En una terminal, iniciar el backend:

```bash
cd backend
uvicorn app.main:app --reload --port 8000
```

En otra terminal, iniciar el frontend:

```bash
cd frontend
npm run dev
```

El frontend estara disponible en `http://localhost:5173` y el backend en `http://localhost:8000`.

## Configuracion con Docker

### 1. Configurar variables de entorno

```bash
cp .env.example .env
# Editar .env con su clave API
```

### 2. Construir y ejecutar

> **Nota:** El backend debe ejecutarse con un solo worker de Uvicorn (configuracion por defecto).
> La persistencia utiliza archivos locales con copia en memoria, por lo que multiples workers o
> replicas tendran estado divergente. Esto es aceptable para MVP.

```bash
docker-compose up --build
```

Los servicios estaran disponibles en:
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000`
- Health check: `http://localhost:8000/health`

### 3. Detener los servicios

```bash
docker-compose down
```

## Variables de Entorno

| Variable | Descripcion | Valor por defecto |
|----------|-------------|-------------------|
| `AI_API_KEY` | Clave API del proveedor de IA | (requerido) |
| `AI_BASE_URL` | URL base del API de IA | `https://integrate.api.nvidia.com/v1` |
| `AI_MODEL` | Modelo de IA a utilizar | `meta/llama-3.1-405b-instruct` |
| `KNOWLEDGE_BASE_PATH` | Ruta a la base de conocimiento | `../skills/knowledge` |
| `STORAGE_PATH` | Ruta para almacenamiento de archivos | `./storage` |

### Proveedores de IA compatibles

El sistema es compatible con cualquier proveedor que implemente la API de OpenAI:

- **NVIDIA NIM**: `https://integrate.api.nvidia.com/v1`
- **OpenAI**: `https://api.openai.com/v1`
- **Ollama (local)**: `http://localhost:11434/v1`
- **Anthropic (via proxy)**: Configurar segun el proxy utilizado

## Fases del Flujo de Investigacion

El sistema guia al usuario a traves de 12 fases secuenciales:

| # | Fase | Descripcion |
|---|------|-------------|
| 1 | **Identificacion del Problema** | El usuario describe la situacion problematica. El sistema identifica el problema. |
| 2 | **Sugerencia de Instrumentos** | El sistema sugiere herramientas para recopilar mas informacion. |
| 3 | **Refinamiento del Problema** | Con los datos recopilados, se generan 3 formulaciones del problema. |
| 4 | **Pregunta de Investigacion** | Se formula la pregunta de investigacion principal. |
| 5 | **Introduccion** | Se genera el capitulo de introduccion. |
| 6 | **Estado de la Cuestion** | El usuario aporta al menos 6 investigaciones similares. Se construye la matriz. |
| 7 | **Planteamiento del Problema** | Se genera el capitulo formal del planteamiento del problema. |
| 8 | **Problemas Especificos** | Se derivan los problemas especificos. |
| 9 | **Objetivo de Investigacion** | Se formula el objetivo general. |
| 10 | **Objetivos Especificos** | Se formulan los objetivos especificos. |
| 11 | **Marco Metodologico** | Se define el marco metodologico con la matriz de conceptualizacion de variables. |
| 12 | **Instrumentos de Recoleccion** | Se disenan los instrumentos de recoleccion de datos. |

En cada fase:
- El sistema valida la **coherencia** de la informacion antes de avanzar
- Se pueden subir archivos (.docx, .xlsx, .md) como insumo
- Al completar un capitulo, se puede generar el documento en formato APA 7

## Base de Conocimiento

La carpeta `skills/knowledge/` contiene aproximadamente 42 archivos Markdown con contenido de libros y guias de metodologia de investigacion:

- Sampieri - Metodologia de la Investigacion
- Vara-Horna - Siete Pasos para una Tesis
- Manual APA 7
- Pautas Metodologicas para Investigaciones
- Guia de Investigacion en Educacion
- Y mas...

El sistema utiliza esta base de conocimiento para:
- Contextualizar las respuestas de la IA con fundamento metodologico
- Aplicar correctamente el metodo cientifico
- Formatear documentos segun APA 7
- Validar la coherencia de cada etapa

El usuario puede tambien subir literatura adicional a traves del endpoint `/knowledge/upload`.

## Resumen de Endpoints API

### Proyectos

| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| POST | `/projects/` | Crear nuevo proyecto |
| GET | `/projects/` | Listar proyectos |
| GET | `/projects/{id}` | Obtener proyecto |
| PUT | `/projects/{id}` | Actualizar proyecto |
| DELETE | `/projects/{id}` | Eliminar proyecto |

### Flujo de Trabajo

| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| GET | `/workflow/{id}/status` | Estado actual del flujo |
| POST | `/workflow/{id}/submit-input` | Enviar texto/archivo para la fase actual |
| POST | `/workflow/{id}/advance` | Avanzar a la siguiente fase |
| POST | `/workflow/{id}/select-option` | Seleccionar opcion (ej. formulacion) |
| POST | `/workflow/{id}/validate` | Validar coherencia de la fase actual |

### Documentos

| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| POST | `/documents/{id}/generate/{chapter}` | Generar documento APA 7 |
| GET | `/documents/{id}/download/{chapter}` | Descargar documento |
| GET | `/documents/{id}/list` | Listar documentos generados |

### Base de Conocimiento

| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| GET | `/knowledge/search?q=query` | Buscar en la base de conocimiento |
| GET | `/knowledge/documents` | Listar documentos disponibles |
| POST | `/knowledge/upload` | Subir literatura adicional |

### Sistema

| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| GET | `/health` | Verificar estado del servicio |

## Ejecucion de Tests

### Backend

```bash
cd backend
source venv/bin/activate
pytest tests/ -v
```

### Frontend

```bash
cd frontend
npm test
```

## Tecnologias Utilizadas

- **Backend**: FastAPI, Uvicorn, Pydantic, OpenAI SDK, python-docx, openpyxl
- **Frontend**: React 19, TypeScript, Vite, Tailwind CSS 4, TanStack Query, React Router, Axios
- **Testing**: pytest (backend), Vitest + Testing Library (frontend)
- **Despliegue**: Docker, Docker Compose, Nginx

## Licencia

Proyecto privado - Todos los derechos reservados.
