# 📋 Task Tracker - Produktivitetsapplikation

En fullstack webbapplikation för att hantera uppgifter och öka produktiviteten. Byggd med FastAPI (backend) och React (frontend) med PostgreSQL databas.

## 📚 Projektöversikt

Detta projekt är en del av kursarbetet "Webbramverk" och demonstrerar:
- ✅ CRUD-operationer (Create, Read, Update, Delete)
- ✅ REST API med FastAPI
- ✅ React frontend med Tailwind CSS
- ✅ PostgreSQL databas med SQLAlchemy ORM
- ✅ Komponentbaserad arkitektur

## 🎯 Funktioner

### Kärnfunktionalitet (CRUD)
- **CREATE**: Skapa nya tasks med titel, beskrivning, prioritet, status och deadline
- **READ**: Visa lista med alla tasks, filtrera efter status och prioritet
- **UPDATE**: Redigera befintliga tasks, ändra status via snabbval
- **DELETE**: Ta bort tasks med bekräftelse

### Extra funktioner
- 📊 Statistik dashboard (total, todo, doing, done)
- 🎨 Responsiv design med Tailwind CSS
- 🔍 Filtrering efter status och prioritet
- ⏰ Visuell indikator för försenade tasks
- 📈 Progress bar för slutförda tasks
- 🎯 Färgkodade prioriteter och statusar

## 🛠️ Teknisk Stack

### Backend
- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: ORM för databashantering
- **PostgreSQL**: Relationsdatabas
- **Pydantic**: Datavalidering

### Frontend
- **React**: UI-bibliotek
- **Vite**: Build tool och dev server
- **Tailwind CSS**: Utility-first CSS framework
- **Fetch API**: HTTP-requests till backend

## 📁 Projektstruktur

```
task-tracker/
├── backend/
│   ├── main.py              # FastAPI app med alla endpoints
│   ├── requirements.txt     # Python dependencies
│   └── .env.example         # Exempel på miljövariabler
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── TaskForm.jsx      # Formulär för skapa/redigera
│   │   │   ├── TaskList.jsx      # Lista med alla tasks
│   │   │   ├── TaskCard.jsx      # Individuell task-vy
│   │   │   ├── TaskStats.jsx     # Statistik dashboard
│   │   │   └── FilterBar.jsx     # Filter-komponenter
│   │   ├── App.jsx               # Huvudkomponent
│   │   ├── main.jsx              # React entrypoint
│   │   └── index.css             # Tailwind CSS
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
└── README.md
```

## 🚀 Installation & Konfiguration

### Förutsättningar
- Python 3.8+
- Node.js 18+
- PostgreSQL 12+

### 1. Klona projektet
```bash
git clone <repository-url>
cd task-tracker
```

### 2. Setup Backend

```bash
cd backend

# Skapa virtuell miljö
python -m venv venv
source venv/bin/activate  # På Windows: venv\Scripts\activate

# Installera dependencies
pip install -r requirements.txt

# Konfigurera databas
# Skapa en PostgreSQL databas:
# createdb tasktracker

# Skapa .env fil
cp .env.example .env
# Redigera .env och uppdatera DATABASE_URL med dina uppgifter
```

### 3. Setup Frontend

```bash
cd ../frontend

# Installera npm packages
npm install
```

## ▶️ Kör Applikationen

### Starta Backend (Terminal 1)
```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend körs nu på: `http://localhost:8000`
API dokumentation: `http://localhost:8000/docs`

### Starta Frontend (Terminal 2)
```bash
cd frontend
npm run dev
```

Frontend körs nu på: `http://localhost:3000`

## 📡 API Endpoints

### Tasks
- `GET /tasks/` - Hämta alla tasks (med optional filters: status, priority)
- `GET /tasks/{task_id}` - Hämta specifik task
- `POST /tasks/` - Skapa ny task
- `PUT /tasks/{task_id}` - Uppdatera task
- `DELETE /tasks/{task_id}` - Ta bort task

### Statistik
- `GET /tasks/stats/summary` - Hämta sammanfattande statistik

### Exempel API Request (Create Task)
```json
POST /tasks/
{
  "title": "Slutför projektarbete",
  "description": "Implementera frontend komponenter",
  "priority": "high",
  "status": "doing",
  "deadline": "2025-02-15T23:59:00"
}
```

## 🎓 Kurskrav - Uppfyllda

### Del 1: HTML & CSS Prototyp ✅
- Designat professionellt gränssnitt med Tailwind CSS
- Responsiv layout med modern design

### Del 2: React + API Integration ✅
- Implementerat alla komponenter i React
- Fetch API för kommunikation med backend
- State management med hooks (useState, useEffect)

### Del 3: Fullstack CRUD-applikation ✅

**Godkänd-nivå:**
- ✅ CREATE: Skapa tasks med formulär
- ✅ READ: Visa och filtrera tasks
- ✅ UPDATE: Redigera tasks och ändra status
- ✅ DELETE: Ta bort tasks med bekräftelse
- ✅ Frontend i React med Tailwind CSS
- ✅ Backend i FastAPI med PostgreSQL
- ✅ Professionell design

**Möjliga VG-förbättringar:**
- Deployment (Render/Railway för backend, Vercel/Netlify för frontend)
- Authentication med JWT
- Asynkron funktionalitet (t.ex. email notifications)
- Caching med Redis
- WebSockets för real-time updates
- AI-integration för task suggestions
- Export till PDF/CSV

## 🧪 Testning

### Manuell testning
1. Skapa en task och verifiera att den syns i listan
2. Uppdatera task status via dropdown
3. Redigera task och kontrollera ändringar
4. Ta bort task och bekräfta
5. Filtrera efter status och prioritet
6. Kontrollera att statistiken uppdateras korrekt

### API-testning
Besök `http://localhost:8000/docs` för interaktiv API-dokumentation (Swagger UI)

## 🔧 Troubleshooting

**Backend startar inte:**
- Kontrollera att PostgreSQL är igång
- Verifiera DATABASE_URL i .env filen
- Kontrollera att alla dependencies är installerade

**Frontend kan inte ansluta till API:**
- Kontrollera att backend körs på port 8000
- Verifiera CORS-inställningar i backend/main.py
- Kontrollera API_URL i frontend/src/App.jsx

**Databas-fel:**
- Kontrollera att databasen "tasktracker" existerar
- Kör migrations om tabeller saknas (SQLAlchemy skapar automatiskt)

## 👥 Utvecklare

- **Ditt namn här**

## 📝 Licens

Detta projekt är utvecklat som en del av kursarbetet på Noroff.

## 🙏 Acknowledgments

- FastAPI documentation
- React documentation
- Tailwind CSS
- PostgreSQL
