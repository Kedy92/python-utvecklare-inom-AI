# Deployment Guide - Task Tracker

## Översikt

Denna guide visar hur du deployar Task Tracker till produktion för VG-nivå demonstration.

**Stack:**
- Backend: Render / Railway
- Frontend: Vercel / Netlify  
- Database: Render PostgreSQL / Supabase

## Del 1: Database (PostgreSQL på Render)

### Steg 1: Skapa PostgreSQL databas på Render

1. Gå till [Render.com](https://render.com)
2. Skapa konto (gratis tier finns)
3. Klicka "New +" → "PostgreSQL"
4. Konfigurera:
   - Name: `task-tracker-db`
   - Region: `Frankfurt` (närmast Sverige)
   - PostgreSQL Version: `16`
   - Plan: `Free`
5. Klicka "Create Database"
6. Vänta 2-3 minuter tills databasen är redo

### Steg 2: Hämta Connection String

1. På dashboard, kopiera "External Database URL"
2. Format: `postgresql://user:password@host:port/database`
3. Spara denna för backend deployment

**Exempel:**
```
postgresql://taskdb_user:xXxPassword123xXx@dpg-abc123.frankfurt-postgres.render.com/taskdb_xyz
```

## Del 2: Backend Deployment (FastAPI på Render)

### Steg 1: Förbered kod för deployment

Skapa `render.yaml` i root:

```yaml
services:
  - type: web
    name: task-tracker-api
    env: python
    region: frankfurt
    buildCommand: pip install -r backend/requirements.txt
    startCommand: cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: DATABASE_URL
        sync: false
      - key: PYTHON_VERSION
        value: 3.11.0
```

Lägg till i `backend/requirements.txt`:
```
gunicorn==21.2.0
```

### Steg 2: Uppdatera main.py för deployment

```python
# I main.py, uppdatera DATABASE_URL läsning:
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Render använder postgres://, men SQLAlchemy kräver postgresql://
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
```

### Steg 3: Deploy till Render

1. Pusha kod till GitHub
2. Gå till Render dashboard
3. Klicka "New +" → "Web Service"
4. Anslut GitHub repository
5. Konfigurera:
   - Name: `task-tracker-api`
   - Region: `Frankfurt`
   - Branch: `main`
   - Build Command: `pip install -r backend/requirements.txt`
   - Start Command: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Lägg till Environment Variables:
   - `DATABASE_URL`: (paste från databas)
7. Klicka "Create Web Service"
8. Vänta 5-10 minuter

### Steg 4: Verifiera Backend

Din API är nu live på: `https://task-tracker-api.onrender.com`

Testa:
- `https://task-tracker-api.onrender.com/` → Ska returnera {"message": "Task Tracker API is running"}
- `https://task-tracker-api.onrender.com/docs` → Swagger UI

## Del 3: Frontend Deployment (React på Vercel)

### Steg 1: Förbered frontend för deployment

Uppdatera `frontend/src/App.jsx`:

```javascript
// Använd environment variable för API URL
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
```

Skapa `.env.production` i frontend/:
```
VITE_API_URL=https://task-tracker-api.onrender.com
```

### Steg 2: Deploy till Vercel

1. Gå till [Vercel.com](https://vercel.com)
2. Logga in med GitHub
3. Klicka "Add New" → "Project"
4. Importera GitHub repository
5. Konfigurera:
   - Framework Preset: `Vite`
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`
6. Environment Variables:
   - `VITE_API_URL`: `https://task-tracker-api.onrender.com`
7. Klicka "Deploy"
8. Vänta 2-3 minuter

### Steg 3: Uppdatera CORS i Backend

I `backend/main.py`, lägg till Vercel URL till CORS:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "https://task-tracker-frontend.vercel.app",  # Din Vercel URL
        "https://task-tracker-*.vercel.app",  # Preview deployments
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Commit och push. Render kommer auto-deploya igen.

## Del 4: Custom Domain (Optional)

### Vercel Custom Domain
1. I Vercel project settings → Domains
2. Lägg till: `tasktracker.dittnamn.se`
3. Följ DNS-instruktioner

### Render Custom Domain  
1. I Render service settings → Custom Domains
2. Lägg till: `api.tasktracker.dittnamn.se`
3. Följ DNS-instruktioner

## Alternativ: Railway Deployment

### Railway (Backend + Database)

1. Gå till [Railway.app](https://railway.app)
2. Logga in med GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Välj repository
5. Railway upptäcker automatiskt FastAPI
6. Lägg till PostgreSQL:
   - Klicka "+ New" → "Database" → "PostgreSQL"
7. Environment Variables sätts automatiskt
8. Deploy!

**Fördel med Railway:** Enklare setup, auto-detects Python

## Troubleshooting

### Problem: Backend timeout på första request
**Lösning:** Render free tier "sleeper" efter 15 min inaktivitet. Första requesten tar ~30 sek.

### Problem: CORS error
**Lösning:** 
1. Kontrollera att Vercel URL är i `allow_origins`
2. Verifiera att backend returnerar CORS headers
3. Testa med curl: `curl -H "Origin: https://din-frontend.vercel.app" https://din-backend.onrender.com/tasks/`

### Problem: Database connection error
**Lösning:**
1. Verifiera DATABASE_URL är korrekt
2. Kontrollera att `postgres://` är ändrat till `postgresql://`
3. Testa connection string lokalt

### Problem: Environment variables inte laddas
**Lösning:**
1. På Render: Gå till Environment → Add environment variable
2. På Vercel: Gå till Settings → Environment Variables
3. Redeploya efter att ha lagt till variables

## Monitoring & Logs

### Render Logs
```bash
# Live logs i dashboard
Render Dashboard → Service → Logs (real-time)
```

### Vercel Logs  
```bash
# Deployment logs
Vercel Dashboard → Deployment → View Function Logs
```

## Performance Tips

### Backend Optimization
1. **Caching**: Implementera Redis för task lists
2. **Database Indexing**: Lägg till index på frequently queried fields
3. **Connection Pooling**: Konfigurera SQLAlchemy pool size

### Frontend Optimization
1. **Code Splitting**: Lazy load components
2. **Image Optimization**: Använd Vercel Image Optimization
3. **Caching**: Service Workers för offline support

## Kostnad (Med Free Tiers)

- **Render PostgreSQL**: Gratis (limited storage)
- **Render Web Service**: Gratis (sleeps after 15 min)
- **Vercel**: Gratis (100GB bandwidth/month)

**Total kostnad: 0 SEK/månad** för development/portfolio

För production med high availability:
- Render PostgreSQL: $7/month
- Render Web Service: $7/month  
- Vercel Pro: $20/month
**Total: ~$34/month (~350 SEK)**

## CI/CD Pipeline

### Automatisk Deployment

**På GitHub push:**
1. GitHub webhook → Render auto-deploy backend
2. GitHub webhook → Vercel auto-deploy frontend

**Workflow:**
```bash
git add .
git commit -m "feat: Add new feature"
git push origin main

# Automatiskt:
# - Render builds och deployar backend
# - Vercel builds och deployar frontend
# - Live på 2-3 minuter!
```

## Deployment Checklist

- [ ] PostgreSQL databas skapad på Render
- [ ] Backend deployad till Render/Railway
- [ ] Environment variables konfigurerade
- [ ] Database migrations körda
- [ ] API endpoints testade i produktion
- [ ] Frontend deployad till Vercel
- [ ] CORS konfigurerat korrekt
- [ ] API URL uppdaterad i frontend
- [ ] Produktion testning genomförd
- [ ] Custom domain konfigurerat (optional)
- [ ] Monitoring/logging verifierat

---

**Efter deployment, inkludera dessa länkar i din README:**

- Live App: https://task-tracker-frontend.vercel.app
- API Docs: https://task-tracker-api.onrender.com/docs
- GitHub: https://github.com/username/task-tracker

Detta är professionellt och visar att du kan deploya fullstack appar! ✨
