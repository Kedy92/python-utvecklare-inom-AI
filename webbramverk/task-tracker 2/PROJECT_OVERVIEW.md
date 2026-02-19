# 📋 Task Tracker - Komplett Projektöversikt

## 🎯 Projektbeskrivning

En fullstack Task/Productivity Tracker byggd med FastAPI (backend) och React (frontend) med PostgreSQL databas. Uppfyller alla krav för kursen "Webbramverk" på Noroff.

---

## 📁 Projektstruktur

```
task-tracker/
├── README.md                      # Huvuddokumentation
├── PROJECT_PLAN.md                # Agil projektplan med veckoschema
├── KURSKRAV_CHECKLISTA.md         # Checklista för alla kurskrav
├── QUICKSTART.md                  # Snabbstartsguide och FAQ
├── DEPLOYMENT.md                  # Guide för deployment (VG)
├── MIRO_GUIDE.md                  # Mall för Miro board och brainstorming
├── .gitignore                     # Git ignore fil
│
├── backend/
│   ├── main.py                    # Huvudsaklig FastAPI app med CRUD
│   ├── main_vg.py                 # Utökad version med VG-features
│   ├── requirements.txt           # Python dependencies (grundläggande)
│   ├── requirements-vg.txt        # Python dependencies (VG-nivå)
│   └── .env.example               # Exempel på miljövariabler
│
└── frontend/
    ├── package.json               # Node dependencies
    ├── vite.config.js             # Vite konfiguration
    ├── tailwind.config.js         # Tailwind CSS konfiguration
    ├── postcss.config.js          # PostCSS konfiguration
    ├── index.html                 # HTML entry point
    │
    └── src/
        ├── main.jsx               # React entry point
        ├── App.jsx                # Huvudkomponent med state & API logic
        ├── index.css              # Tailwind CSS imports
        │
        └── components/
            ├── TaskForm.jsx       # Formulär för skapa/redigera tasks
            ├── TaskList.jsx       # Lista med alla tasks
            ├── TaskCard.jsx       # Individuell task-vy
            ├── TaskStats.jsx      # Statistik dashboard
            └── FilterBar.jsx      # Filter-komponenter
```

---

## ✅ Uppfyllda Kurskrav

### Del 1: HTML & CSS Prototyp
✅ Professionellt designade komponenter med Tailwind CSS  
✅ Responsiv layout  
✅ 5+ centrala vyer (Form, List, Card, Stats, Filter)

### Del 2: React + API Integration  
✅ Fullständig React-applikation  
✅ API-integration med FastAPI backend  
✅ State management med hooks  
✅ Interaktiva komponenter

### Del 3: Projektarbete - Godkänd (G)
✅ **CREATE**: Skapa nya tasks via TaskForm  
✅ **READ**: Visa tasks i lista med filtrering  
✅ **UPDATE**: Redigera tasks och ändra status  
✅ **DELETE**: Ta bort tasks med bekräftelse  
✅ Frontend i React med professionell design  
✅ Backend i FastAPI med PostgreSQL  
✅ Miro-board mall förberedd

### Del 3: Projektarbete - Väl Godkänd (VG)
✅ **Asynkron funktionalitet**: Email notifications (background tasks)  
✅ **AI-integration**: OpenAI för task suggestions  
✅ **Schemaläggning**: Periodisk cleanup av tasks  
✅ **Caching**: Redis/in-memory caching för performance  
✅ **Deployment Guide**: Komplett guide för Render + Vercel  
✅ **Avancerad Analytics**: Productivity metrics endpoint  
✅ **Export**: JSON export-funktionalitet  
✅ **Professionell Design**: Tailwind CSS best practices

---

## 🚀 Snabbstart

### Installation

```bash
# 1. Klona projektet
git clone <repository-url>
cd task-tracker

# 2. Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Redigera .env med din DATABASE_URL

# 3. Frontend setup
cd ../frontend
npm install

# 4. Skapa PostgreSQL databas
createdb tasktracker
```

### Kör Applikationen

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

**Öppna:** http://localhost:3000

---

## 📡 API Endpoints

### Tasks CRUD
- `GET /tasks/` - Hämta alla tasks (med filters)
- `GET /tasks/{id}` - Hämta specifik task
- `POST /tasks/` - Skapa ny task
- `PUT /tasks/{id}` - Uppdatera task
- `DELETE /tasks/{id}` - Ta bort task

### Statistik & Extra
- `GET /tasks/stats/summary` - Hämta statistik
- `GET /tasks/cached/` - Cachade tasks (VG)
- `GET /tasks/analytics/productivity` - Produktivitets-analytics (VG)
- `POST /tasks/ai/suggest` - AI task suggestions (VG)
- `POST /tasks/{id}/notify` - Asynkron email notification (VG)
- `GET /tasks/export/json` - Export till JSON (VG)

---

## 💻 Teknisk Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM för databas
- **PostgreSQL** - Produktionsdatabas
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

### Frontend
- **React** - UI library
- **Vite** - Build tool
- **Tailwind CSS** - Utility-first CSS
- **Fetch API** - HTTP client

### VG Features
- **OpenAI** - AI task suggestions
- **Background Tasks** - Asynkron email
- **Redis** - Caching (simulerat)
- **Render** - Backend deployment
- **Vercel** - Frontend deployment

---

## 🎨 Funktioner

### Kärnfunktionalitet
- ✅ Skapa tasks med titel, beskrivning, prioritet, deadline
- ✅ Visa alla tasks i lista
- ✅ Filtrera efter status (todo/doing/done)
- ✅ Filtrera efter prioritet (low/medium/high)
- ✅ Uppdatera task status via dropdown
- ✅ Redigera befintliga tasks
- ✅ Ta bort tasks med bekräftelse
- ✅ Statistik dashboard (total, todo, doing, done)
- ✅ Progress bar för completion rate
- ✅ Visuell indikator för försenade tasks
- ✅ Färgkodade prioriteter och statusar

### VG-funktioner (main_vg.py)
- ⭐ AI-genererade task suggestions
- ⭐ Asynkrona email-notifikationer
- ⭐ Caching för förbättrad performance
- ⭐ Schemalagd cleanup av gamla tasks
- ⭐ Avancerad produktivitets-analytics
- ⭐ Export till JSON
- ⭐ Logging system
- ⭐ Deployment-ready kod

---

## 📚 Dokumentation

### För Studenter
- **README.md** - Huvuddokumentation med installation
- **QUICKSTART.md** - 5-minuters snabbstart + FAQ
- **PROJECT_PLAN.md** - Agil projektplan med veckoschema
- **KURSKRAV_CHECKLISTA.md** - Checklista för alla krav

### För VG-nivå
- **DEPLOYMENT.md** - Komplett deployment guide
- **MIRO_GUIDE.md** - Mall för Miro board
- **main_vg.py** - Avancerade features

---

## 🎯 Användning för Kursen

### Scenario 1: Börja från scratch
1. Läs README.md för översikt
2. Följ QUICKSTART.md för installation
3. Använd PROJECT_PLAN.md för veckoplanering
4. Kryssa av i KURSKRAV_CHECKLISTA.md
5. Jobba agilt enligt planen

### Scenario 2: Direkt till del 3
1. Skapa GitHub repo
2. Kopiera hela projekt-strukturen
3. Bjud in läraren (tobeyforce)
4. Börja committa löpande
5. Implementera VG-features

### Scenario 3: Endast inspiration
1. Studera arkitekturen
2. Ta inspiration från komponenter
3. Bygg egen variant
4. Behåll samma teknisk stack

---

## 🔄 Git Workflow

```bash
# Daglig rutin
git pull origin main
git checkout -b feature/ny-funktion
# ... jobba ...
git add .
git commit -m "feat: beskrivning"
git push origin feature/ny-funktion

# Veckovis merge
git checkout main
git merge feature/ny-funktion
git push origin main
```

**Viktigt:** Minst 3-5 commits per vecka!

---

## ✨ Nästa Steg

1. **Vecka 1**: Setup projekt, implementera CRUD
2. **Vecka 2**: Komplett frontend, integration
3. **Vecka 3**: VG-features, polish
4. **Vecka 4**: Deployment, testing
5. **Vecka 5**: Demo-förberedelse

---

## 🎓 Lärresultat

Efter detta projekt kan du:
- ✅ Bygga fullstack webbapplikationer
- ✅ Arbeta med REST APIs
- ✅ Använda React med modern state management
- ✅ Designa och implementera databaser
- ✅ Deploya till produktion
- ✅ Jobba agilt i team
- ✅ Versionshantera med Git
- ✅ Integrera AI-tjänster
- ✅ Implementera asynkron funktionalitet

---

## 📞 Support

- **Kurs-Discord**: projektarbete kanal
- **Lärare**: tobeyforce
- **Email**: tobias.fors.1993@gmail.com
- **GitHub Issues**: För buggar i projektet

---

## 📝 Licens

Detta projekt är utvecklat som kursmaterial för Noroff.  
Fri att använda för utbildningssyfte.

---

## 🙏 Credits

- **Framework**: FastAPI, React, Tailwind CSS
- **Inspiration**: Produktivitets-appar som Todoist, Trello
- **Kurs**: Webbramverk - Noroff

---

**Senast uppdaterad:** 2025-01-31  
**Version:** 1.0  
**Status:** ✅ Produktionsklar för kursinlämning

**Lycka till med projektet! 🚀**
