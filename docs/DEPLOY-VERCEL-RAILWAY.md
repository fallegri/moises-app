# Deployment Guide: Vercel + Railway + NeonTech

This guide covers deploying the Research Assistant application with:
- **Frontend**: Vercel (React SPA)
- **Backend**: Railway (FastAPI + Uvicorn)
- **Database**: NeonTech (PostgreSQL)

## Architecture Overview

```
[Vercel - Frontend]  -->  [Railway - Backend API]  -->  [NeonTech - PostgreSQL]
     React SPA              FastAPI + Uvicorn             Managed PostgreSQL
```

## Prerequisites

- GitHub repository with the project code
- [Vercel](https://vercel.com) account
- [Railway](https://railway.app) account
- [NeonTech](https://neon.tech) account

---

## 1. NeonTech PostgreSQL Setup

1. Create a new project in [NeonTech Console](https://console.neon.tech)
2. Choose a region close to your Railway deployment (recommended: US East)
3. Copy the connection string. It will look like:
   ```
   postgresql://user:password@ep-xxxxx.us-east-2.aws.neon.tech/neondb?sslmode=require
   ```
4. Save this as your `DATABASE_URL` for the backend configuration

### Database Tables

Tables are created automatically on backend startup when `DATABASE_URL` is configured. You can also create them manually:

```bash
cd backend
DATABASE_URL="your-neon-connection-string" python -m app.db.init_db
```

---

## 2. Railway Backend Deployment

### Setup

1. Go to [Railway Dashboard](https://railway.app/dashboard)
2. Click "New Project" > "Deploy from GitHub repo"
3. Select your repository
4. Set the **Root Directory** to `backend`

### Environment Variables

Configure the following environment variables in Railway:

| Variable | Value | Required |
|----------|-------|----------|
| `DATABASE_URL` | NeonTech connection string | Yes |
| `AI_API_KEY` | Your AI provider API key | Yes |
| `AI_BASE_URL` | AI API base URL (default: NVIDIA) | No |
| `AI_MODEL` | AI model name | No |
| `FRONTEND_URL` | Your Vercel deployment URL (e.g., `https://your-app.vercel.app`) | Yes |
| `STORAGE_PATH` | `/tmp/storage` (for Railway ephemeral storage) | Recommended |

### Railway Configuration

Railway will automatically detect the `Procfile` and `runtime.txt`:
- **Procfile**: `web: uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- **runtime.txt**: `python-3.11`

### Custom Domain (Optional)

1. In Railway project settings, go to "Domains"
2. Add a custom domain or use the generated `.up.railway.app` domain
3. Note this URL for the frontend `VITE_API_URL` configuration

---

## 3. Vercel Frontend Deployment

### Setup

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click "Add New" > "Project"
3. Import your GitHub repository
4. Set the **Root Directory** to `frontend`
5. Framework Preset should auto-detect as "Vite"

### Build Settings

- **Build Command**: `npm run build`
- **Output Directory**: `dist`
- **Install Command**: `npm install`

### Environment Variables

Configure in Vercel project settings:

| Variable | Value | Required |
|----------|-------|----------|
| `VITE_API_URL` | Railway backend URL (e.g., `https://your-backend.up.railway.app`) | Yes |

**Important**: The `VITE_` prefix is required for Vite to expose the variable to the client bundle.

### SPA Routing

The `frontend/vercel.json` file handles SPA routing:
```json
{
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

This ensures all routes are handled by the React router.

---

## 4. CORS Configuration

The backend automatically includes the `FRONTEND_URL` in allowed CORS origins. Make sure:

1. `FRONTEND_URL` in Railway matches your Vercel deployment URL exactly (including `https://`)
2. No trailing slash in the URL

Default CORS origins (always allowed):
- `http://localhost:5173` (Vite dev server)
- `http://localhost:3000` (alternative local dev)

---

## 5. Local Development

For local development, the application falls back to JSON file persistence when `DATABASE_URL` is not set.

### Running locally without PostgreSQL

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# Frontend
cd frontend
npm install
npm run dev
```

### Running locally with PostgreSQL

```bash
# Set DATABASE_URL to a local or NeonTech database
export DATABASE_URL="postgresql://user:password@localhost:5432/research_db"

cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Using Docker Compose (existing setup)

```bash
docker-compose up
```

The Docker Compose setup uses the JSON file persistence by default.

---

## 6. Verification

After deployment, verify:

1. **Backend Health**: `GET https://your-backend.up.railway.app/health`
   - Should return `{"status": "healthy", "service": "Research Assistant API"}`

2. **Frontend**: Visit your Vercel URL
   - The app should load and be able to create projects

3. **Database Connection**: Create a project through the frontend
   - Verify it persists after backend restart

---

## 7. Troubleshooting

### Common Issues

**CORS errors in browser console**
- Verify `FRONTEND_URL` in Railway matches the exact Vercel URL
- Check there is no trailing slash

**Database connection errors**
- Verify the `DATABASE_URL` format includes `?sslmode=require` for NeonTech
- Check NeonTech project is not suspended (free tier suspends after inactivity)

**Frontend shows blank page**
- Check `VITE_API_URL` is set correctly in Vercel
- Redeploy the frontend after changing environment variables (Vite embeds env vars at build time)

**Railway deployment fails**
- Ensure `runtime.txt` contains `python-3.11`
- Check that `requirements.txt` is in the `backend/` root directory
- Verify no syntax errors in the Procfile

### Redeploying

- **Backend**: Push to the configured branch, Railway auto-deploys
- **Frontend**: Push to the configured branch, Vercel auto-deploys
- **Environment variable changes**: 
  - Backend: Railway auto-restarts on env var change
  - Frontend: Must trigger a redeploy (env vars are embedded at build time)
