# Guía de Implementación — Asistente de Investigación

## Índice
1. [Opción 1: Docker (local o VPS)](#opción-1-docker-local-o-vps)
2. [Opción 2: Local sin Docker](#opción-2-local-sin-docker)
3. [Opción 3: Vercel + NeonTech/MongoDB Atlas](#opción-3-vercel-frontend--railwayrender-backend--neontech-o-mongodb)
4. [Opción 4: Railway (Full Stack)](#opción-4-railway-full-stack)

---

## Opción 1: Docker (local o VPS)

### Requisitos previos
- Docker 24+ y Docker Compose v2
- Al menos 2GB de RAM disponible

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/fallegri/moises-app.git
cd moises-app
```

### Paso 2: Construir y levantar los servicios
```bash
docker compose up --build -d
```

### Paso 3: Verificar que todo está corriendo
```bash
docker compose ps
# Deberías ver:
#   backend   - 0.0.0.0:8000->8000/tcp
#   frontend  - 0.0.0.0:3000->3000/tcp

# Verificar health del backend:
curl http://localhost:8000/health
```

### Paso 4: Configurar la API Key de IA
1. Abre `http://localhost:3000` en tu navegador
2. Ve a **Configuración** en el menú de navegación
3. Ingresa tu API Key, URL base y modelo
4. Haz clic en **Guardar**

### Paso 5: Comenzar a usar
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000`
- Docs interactivos: `http://localhost:8000/docs`

### Parar y reiniciar
```bash
docker compose down          # Detener
docker compose up -d         # Reiniciar (datos persisten en volume)
docker compose down -v       # Detener Y borrar datos
```

### Para producción en VPS (DigitalOcean, AWS EC2, etc.)
```bash
# Agregar un reverse proxy con SSL (ejemplo con Caddy)
apt install caddy

# /etc/caddy/Caddyfile
echo '
tudominio.com {
    handle /api/* {
        reverse_proxy localhost:8000
    }
    handle /health {
        reverse_proxy localhost:8000
    }
    handle {
        reverse_proxy localhost:3000
    }
}
' > /etc/caddy/Caddyfile

systemctl restart caddy
```

---

## Opción 2: Local sin Docker

### Requisitos previos
- Python 3.11+
- Node.js 22+
- Git

### Paso 1: Clonar
```bash
git clone https://github.com/fallegri/moises-app.git
cd moises-app
```

### Paso 2: Backend
```bash
cd backend

# Crear entorno virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate    # Windows

# Instalar dependencias
pip install -r requirements.txt

# (Opcional) Crear .env si quieres configurar la key por archivo
# cp .env.example .env
# nano .env

# Iniciar backend
uvicorn app.main:app --reload --port 8000
```

### Paso 3: Frontend (nueva terminal)
```bash
cd frontend

# Instalar dependencias
npm install

# Iniciar dev server
npm run dev
```

### Paso 4: Acceder
- Frontend: `http://localhost:5173`
- Backend: `http://localhost:8000`
- Ir a **Configuración** y registrar tu API Key de IA

### Paso 5: Ejecutar tests
```bash
# Backend
cd backend && pytest tests/ -v

# Frontend
cd frontend && npm test
```

---

## Opción 3: Vercel (Frontend) + Railway/Render (Backend) + NeonTech o MongoDB

> **Nota importante:** Vercel solo sirve para el frontend (es serverless/estático). El backend FastAPI necesita un host con soporte a procesos persistentes (Railway, Render, Fly.io). Si necesitas base de datos, usa NeonTech (PostgreSQL) o MongoDB Atlas.

### Paso 3.1: Preparar el Backend para Base de Datos

Actualmente el sistema usa persistencia en JSON files. Para producción con NeonTech o MongoDB, necesitas migrar la persistencia:

**Opción A — NeonTech (PostgreSQL serverless):**

1. Crea cuenta en [neon.tech](https://neon.tech)
2. Crea un nuevo proyecto y obtén la connection string:
   ```
   postgresql://user:password@ep-xxx.us-east-2.aws.neon.tech/dbname?sslmode=require
   ```
3. Agrega `DATABASE_URL` como variable de entorno en el backend

**Opción B — MongoDB Atlas:**

1. Crea cuenta en [mongodb.com/atlas](https://www.mongodb.com/atlas)
2. Crea un cluster gratuito (M0) y obtén la connection string:
   ```
   mongodb+srv://user:password@cluster0.xxx.mongodb.net/research_assistant
   ```
3. Agrega `MONGODB_URL` como variable de entorno en el backend

> **Nota:** La migración a base de datos requiere un cambio en el código del backend (reemplazar `persistence.py`). Por ahora, para un MVP funcional, el sistema trabaja con JSON files — lo cual es totalmente viable en Railway/Render con disco persistente.

### Paso 3.2: Desplegar Backend en Railway

1. Crea cuenta en [railway.app](https://railway.app)
2. Conecta tu repositorio de GitHub
3. Railway detectará el backend automáticamente. Si no, configura:
   - **Root Directory:** `backend`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. Variables de entorno en Railway:
   ```
   STORAGE_PATH=/app/storage
   KNOWLEDGE_BASE_PATH=/app/knowledge
   CORS_ORIGINS=["https://tu-app.vercel.app"]
   ```
5. Sube la carpeta `skills/knowledge/` como volumen o inclúyela en el build
6. Anota la URL del servicio: `https://tu-backend.up.railway.app`

### Paso 3.3: Desplegar Frontend en Vercel

1. Crea cuenta en [vercel.com](https://vercel.com)
2. Importa el repositorio de GitHub
3. Configura:
   - **Root Directory:** `frontend`
   - **Framework Preset:** Vite
   - **Build Command:** `npm run build`
   - **Output Directory:** `dist`
4. **Variable de entorno crucial:**
   ```
   VITE_API_URL=https://tu-backend.up.railway.app
   ```
5. Verifica que el frontend apunte al backend. Busca en `frontend/src/api/` la URL base y asegúrate de que usa `import.meta.env.VITE_API_URL`:
   ```typescript
   const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
   ```

### Paso 3.4: Configurar CORS

En el backend, asegúrate de que `CORS_ORIGINS` incluya tu dominio de Vercel:
```
CORS_ORIGINS=["https://moises-app.vercel.app","http://localhost:5173"]
```

### Paso 3.5: Verificar

1. Abre `https://tu-app.vercel.app`
2. Ve a **Configuración** e ingresa tu API Key
3. Crea un proyecto y comienza tu investigación

---

## Opción 4: Railway (Full Stack)

> Railway puede hospedar ambos servicios (backend + frontend) con un solo repositorio.

### Paso 1: Crear cuenta y proyecto

1. Ve a [railway.app](https://railway.app) y regístrate con GitHub
2. Crea un **New Project** → **Deploy from GitHub repo**
3. Selecciona `fallegri/moises-app`

### Paso 2: Configurar servicio Backend

1. Click en **+ New Service** → selecciona el mismo repo
2. Configura:
   - **Name:** `backend`
   - **Root Directory:** `backend`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
3. Variables de entorno:
   ```
   STORAGE_PATH=/app/storage
   KNOWLEDGE_BASE_PATH=/app/knowledge
   ```
4. Genera un dominio público: Settings → Networking → Generate Domain
   - Obtendrás algo como: `backend-production-xxxx.up.railway.app`

### Paso 3: Agregar volumen para persistencia

1. En el servicio backend → **+ New** → **Volume**
2. Mount path: `/app/storage`
3. Esto persiste los proyectos, workflows y configuración de AI entre deploys

### Paso 4: Subir la base de conocimiento

Opción A — Incluir en el Dockerfile:
```dockerfile
# Agregar al Dockerfile del backend, antes del CMD:
COPY ../skills/knowledge /app/knowledge
```

Opción B — Usar un volumen adicional y subir manualmente vía API (`/api/knowledge/upload`)

### Paso 5: Configurar servicio Frontend

1. **+ New Service** → mismo repo
2. Configura:
   - **Name:** `frontend`
   - **Root Directory:** `frontend`
   - **Build Command:** `npm install && npm run build`
   - **Start Command:** `npx serve dist -l $PORT`
   - (O usar el Dockerfile con nginx)
3. Variables de entorno:
   ```
   VITE_API_URL=https://backend-production-xxxx.up.railway.app
   ```
4. Genera dominio público para el frontend

### Paso 6: Configurar networking interno (alternativa)

Railway permite networking privada entre servicios:
- Backend puede ser accesible internamente como `backend.railway.internal:8000`
- Pero para el frontend (que corre en el navegador del usuario), necesitas la URL pública del backend

### Paso 7: Verificar el despliegue

```bash
# Health check
curl https://backend-production-xxxx.up.railway.app/health

# Respuesta esperada:
# {"status":"healthy","service":"Research Assistant API"}
```

### Paso 8: Configurar IA desde la UI

1. Abre `https://frontend-production-xxxx.up.railway.app`
2. Menú → **Configuración**
3. Registra tu API Key de IA
4. ¡Listo para investigar!

---

## Resumen de costos estimados

| Plataforma | Tier Gratuito | Costo Producción |
|---|---|---|
| **Docker (VPS)** | — | ~$5-12/mes (DigitalOcean/Hetzner) |
| **Railway** | 500 hrs/mes gratis | ~$5/mes por servicio |
| **Vercel** | Hobby tier gratuito | $0 (frontend) |
| **NeonTech** | 0.5 GB gratis | ~$19/mes (Pro) |
| **MongoDB Atlas** | 512 MB gratis | ~$9/mes (M2) |

---

## Notas importantes

1. **La API Key de IA se configura desde la UI** — no necesitas configurarla en variables de entorno del hosting
2. **La base de conocimiento** (42 archivos .md) debe estar accesible al backend en la ruta configurada en `KNOWLEDGE_BASE_PATH`
3. **Para escalar** a múltiples usuarios simultáneos, migra de JSON persistence a PostgreSQL (NeonTech) o MongoDB
4. **SSL/HTTPS** es automático en Vercel y Railway. En Docker/VPS necesitas un reverse proxy (Caddy, Nginx + Certbot)
