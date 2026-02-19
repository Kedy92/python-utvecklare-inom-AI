# Snabbstart Guide - Task Tracker

## 🚀 Quick Start (5 minuter)

### Förutsättningar installerade?
```bash
python --version  # Ska visa 3.8+
node --version    # Ska visa 18+
psql --version    # Ska visa PostgreSQL
```

### Steg 1: Klona & Setup (2 min)

```bash
# Klona projektet
git clone https://github.com/ditt-username/task-tracker.git
cd task-tracker

# Skapa PostgreSQL databas
createdb tasktracker

# Eller via psql:
psql
CREATE DATABASE tasktracker;
\q
```

### Steg 2: Backend Setup (1 min)

```bash
cd backend

# Skapa virtual environment
python -m venv venv

# Aktivera (Mac/Linux)
source venv/bin/activate

# Aktivera (Windows)
venv\Scripts\activate

# Installera dependencies
pip install -r requirements.txt

# Skapa .env
cp .env.example .env

# Redigera .env med din databas-info
# DATABASE_URL=postgresql://user:password@localhost:5432/tasktracker
```

### Steg 3: Frontend Setup (1 min)

```bash
cd ../frontend

# Installera npm packages
npm install
```

### Steg 4: Kör! (1 min)

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # Aktivera venv
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### Steg 5: Testa!

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

**Första testet:**
1. Skapa en task i formuläret
2. Se att den dyker upp i listan
3. Uppdatera status via dropdown
4. Klicka "Redigera"
5. Ta bort tasken

✅ **Fungerar det? Grattis, du är igång!**

---

## 🔧 Detaljerade Setup-instruktioner

### PostgreSQL Setup (Om du inte har det)

**Mac:**
```bash
brew install postgresql@16
brew services start postgresql@16
createdb tasktracker
```

**Ubuntu/Linux:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo service postgresql start
sudo -u postgres createdb tasktracker
```

**Windows:**
1. Ladda ner från: https://www.postgresql.org/download/windows/
2. Installera PostgreSQL
3. Öppna pgAdmin eller psql
4. Skapa databas `tasktracker`

### Databas Connection String

Format:
```
postgresql://[user]:[password]@[host]:[port]/[database]
```

**Exempel:**
```bash
# Lokalt med default postgres user
postgresql://postgres:postgres@localhost:5432/tasktracker

# Lokalt med egen user
postgresql://myuser:mypassword@localhost:5432/tasktracker

# Render (produktion)
postgresql://user:pass@dpg-xyz.frankfurt-postgres.render.com/taskdb
```

---

## 🐛 Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'fastapi'"

**Lösning:**
```bash
# Aktivera virtual environment först!
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Sedan installera
pip install -r requirements.txt
```

### Problem: "could not connect to server: Connection refused"

**Lösning:** PostgreSQL körs inte

```bash
# Mac
brew services start postgresql@16

# Linux
sudo service postgresql start

# Windows
# Starta PostgreSQL service via Services
```

### Problem: "database "tasktracker" does not exist"

**Lösning:**
```bash
createdb tasktracker

# Eller via psql
psql
CREATE DATABASE tasktracker;
\q
```

### Problem: "CORS error" i browsern

**Lösning:** Kontrollera att:
1. Backend körs på port 8000
2. Frontend körs på port 3000 eller 5173
3. CORS är konfigurerat i `main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    ...
)
```

### Problem: "Port 8000 already in use"

**Lösning:**
```bash
# Hitta process
lsof -i :8000  # Mac/Linux
netstat -ano | findstr :8000  # Windows

# Döda process
kill -9 <PID>  # Mac/Linux
taskkill /PID <PID> /F  # Windows

# Eller använd annan port
uvicorn main:app --reload --port 8001
```

### Problem: React app visar tom sida

**Lösning:**
```bash
# Kontrollera console i browser (F12)
# Ofta saknas node_modules

cd frontend
npm install
npm run dev
```

### Problem: "Cannot find module './components/TaskForm'"

**Lösning:** Komponenten finns inte än
```bash
# Skapa alla komponenter från detta projekt
# Se frontend/src/components/ mappen
```

---

## 💡 Tips & Best Practices

### Git Workflow

```bash
# Börja dagen
git pull origin main

# Skapa feature branch
git checkout -b feature/task-filtering

# Jobba och commita ofta
git add .
git commit -m "feat: Add priority filtering"

# Pusha dagligen
git push origin feature/task-filtering

# När klar, merga till main
git checkout main
git merge feature/task-filtering
git push origin main
```

### Commit Messages

**Bra:**
```
feat: Add task filtering by status
fix: Resolve deadline date display issue
docs: Update README with deployment guide
style: Format TaskCard component
refactor: Simplify API error handling
```

**Dåligt:**
```
update
fixed bug
changes
idk
asdf
```

### Development Workflow

1. **Morgon:**
   - Pull latest changes
   - Planera dagens arbete
   - Skapa feature branch

2. **Under dagen:**
   - Commit ofta (var 30-60 min)
   - Testa efter varje funktion
   - Push minst en gång per dag

3. **Kväll:**
   - Code review av dagens arbete
   - Uppdatera Miro board
   - Planera nästa dag

---

## 📚 Vanliga Frågor (FAQ)

### Q: Hur många timmar ska jag lägga på projektet?

**A:** Rekommenderat minimum är 40h/vecka i 4-5 veckor. För VG, sikta på 50-60h/vecka. Det är intensivt men ger extremt mycket lärande!

### Q: Kan jag använda [X framework] istället för FastAPI?

**A:** Nej, kurskravet är FastAPI och React. Undantag kräver lärarens godkännande vilket sällan ges.

### Q: Måste jag använda PostgreSQL? Kan jag inte bara använda SQLite?

**A:** Kurskravet specificerar PostgreSQL. SQLite är enklare men mindre realistiskt för produktion. Använd PostgreSQL!

### Q: Hur mycket ska jag kommentera koden?

**A:** Kommentera INTE överdrivet. Skriv kod som är självförklarande. Kommentera endast:
- Komplexa algoritmer
- Varför något görs (inte vad)
- API endpoints (docstrings)

**Dåligt:**
```python
# create a variable for the name
name = "Task"  

# add one to the counter
counter = counter + 1
```

**Bra:**
```python
# Cache results for 5 minutes to reduce database load
@cache(ttl=300)
def get_tasks():
    ...
```

### Q: Kan jag använda AI (ChatGPT, Copilot) för att koda?

**A:** Ja, MEN du måste förstå all kod. Om du inte kan förklara varje rad så kommer du bli kompleterad. Använd AI för:
- Syntax-hjälp
- Debugging
- Optimering
- Idéer

Använd INTE AI för:
- Kopiera hela lösningar
- Generera kod du inte förstår
- Ersätta eget lärande

### Q: Hur många commits behöver jag?

**A:** Minst 30-50 commits totalt, spridda över projekttiden. ALDRIG en enda commit i slutet!

### Q: Vad händer om min partner inte bidrar?

**A:** Kommunicera direkt med läraren. Ni bedöms individuellt baserat på era commits och kunskaper.

### Q: Måste jag deploya för godkänt?

**A:** Nej, deployment är VG-nivå. Men det är starkt rekommenderat för portfolio!

### Q: Hur lång ska demo-presentationen vara?

**A:** 5-10 minuter demo + 5-10 minuter frågor. Fokus på att VISA funktionaliteten, inte förklara koden i detalj.

### Q: Kan jag byta idé efter att ha börjat?

**A:** Ja, men ju tidigare desto bättre. Efter vecka 3 är det svårt.

### Q: Vad är viktigast för VG?

**A:** 
1. Avancerad funktionalitet (AI, async, deployment)
2. Stark förståelse (kan svara på alla frågor)
3. God kodkvalitet och historik
4. Imponerande demo

---

## 🎯 Nästa Steg

1. **Vecka 1:** Kör igenom denna snabbstart-guide
2. **Vecka 2:** Implementera alla CRUD-funktioner
3. **Vecka 3:** Polera frontend, lägg till VG-features
4. **Vecka 4:** Deploy, testing, bugfix
5. **Vecka 5:** Förbered demo

**Du klarar detta! 💪**

---

## 📞 Support & Resurser

**Kursmaterial:**
- Discord: Se `projektarbete` kanal
- Läroportalen: Deadlines och uppgifter

**Teknisk hjälp:**
- FastAPI docs: https://fastapi.tiangolo.com/
- React docs: https://react.dev/
- PostgreSQL tutorial: https://www.postgresqltutorial.com/

**Community:**
- Stack Overflow
- Reddit r/FastAPI, r/reactjs
- Discord klasskanal

**Lärare:**
- Boka handledning via Discord
- Veckoavstämningar obligatoriska

---

**Senast uppdaterad:** 2025-01-31  
**Version:** 1.0  
**Författare:** Task Tracker Team
