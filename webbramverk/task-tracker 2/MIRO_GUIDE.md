# Miro Board - Task Tracker Projektet

## Länk till Miro Board
[Lägg till din Miro board länk här]

## Hur man skapar Miro Board

1. Gå till https://miro.com
2. Skapa gratis konto
3. Skapa ny board: "Task Tracker - Projektarbete"
4. Bjud in din projektpartner
5. Bjud in läraren (tobeyforce)

## Förslag på Board-struktur

### Sektion 1: BRAINSTORMING & IDÉ
```
┌─────────────────────────────────────────┐
│         PROJEKTIDÉ                       │
│                                          │
│  Task Tracker - Productivity App        │
│                                          │
│  Problem: Svårt att hålla koll på      │
│  uppgifter och prioritera               │
│                                          │
│  Lösning: Enkel, visuell task-hantering│
│  med prioriteringar och deadlines       │
│                                          │
│  Target Users:                          │
│  - Studenter                            │
│  - Utvecklare                           │
│  - Alla som behöver organisera tasks    │
└─────────────────────────────────────────┘
```

### Sektion 2: USER STORIES
```
Som användare vill jag kunna:
┌──────────────────────────────────────┐
│ ✓ Skapa nya tasks med titel och     │
│   beskrivning                        │
├──────────────────────────────────────┤
│ ✓ Sätta prioritet (low/medium/high) │
├──────────────────────────────────────┤
│ ✓ Sätta deadlines för tasks         │
├──────────────────────────────────────┤
│ ✓ Uppdatera task status             │
│   (todo/doing/done)                 │
├──────────────────────────────────────┤
│ ✓ Filtrera tasks efter status och   │
│   prioritet                         │
├──────────────────────────────────────┤
│ ✓ Se statistik över mina tasks      │
├──────────────────────────────────────┤
│ ✓ Ta bort tasks jag inte längre     │
│   behöver                           │
└──────────────────────────────────────┘

VG User Stories:
┌──────────────────────────────────────┐
│ □ Få AI-hjälp med task-suggestions  │
├──────────────────────────────────────┤
│ □ Få email-påminnelser om deadlines │
├──────────────────────────────────────┤
│ □ Exportera tasks till JSON/CSV     │
├──────────────────────────────────────┤
│ □ Se produktivitets-analytics       │
└──────────────────────────────────────┘
```

### Sektion 3: TEKNISK ARKITEKTUR
```
┌─────────────────────────────────────────┐
│           SYSTEM DESIGN                  │
│                                          │
│  Frontend (React)                        │
│  ├── App.jsx (main)                     │
│  ├── TaskForm.jsx                       │
│  ├── TaskList.jsx                       │
│  ├── TaskCard.jsx                       │
│  ├── TaskStats.jsx                      │
│  └── FilterBar.jsx                      │
│                                          │
│         ↕ (HTTP/REST)                   │
│                                          │
│  Backend (FastAPI)                      │
│  ├── GET /tasks/                        │
│  ├── POST /tasks/                       │
│  ├── PUT /tasks/{id}                    │
│  ├── DELETE /tasks/{id}                 │
│  └── GET /tasks/stats/summary           │
│                                          │
│         ↕ (SQLAlchemy ORM)              │
│                                          │
│  Database (PostgreSQL)                  │
│  └── tasks (table)                      │
│      ├── id (PK)                        │
│      ├── title                          │
│      ├── description                    │
│      ├── priority                       │
│      ├── status                         │
│      ├── deadline                       │
│      ├── created_at                     │
│      └── updated_at                     │
└─────────────────────────────────────────┘
```

### Sektion 4: DATABASE SCHEMA
```
┌─────────────────────────────────────┐
│         tasks                        │
├─────────────────────────────────────┤
│ PK │ id              │ INTEGER      │
│    │ title           │ VARCHAR(255) │
│    │ description     │ TEXT         │
│    │ priority        │ ENUM         │
│    │ status          │ ENUM         │
│    │ deadline        │ TIMESTAMP    │
│    │ created_at      │ TIMESTAMP    │
│    │ updated_at      │ TIMESTAMP    │
│    │ ai_generated    │ TEXT         │
└─────────────────────────────────────┘

Enums:
- priority: low, medium, high
- status: todo, doing, done
```

### Sektion 5: UI/UX WIREFRAMES
```
┌──────────────────────────────────────────┐
│  📋 Task Tracker                         │
├──────────────────────────────────────────┤
│                                          │
│  [Total: 12] [Todo: 5] [Doing: 4] [✓: 3]│
│  ▓▓▓░░░░░░░ 25% Complete                │
│                                          │
│  Filter: [All Status ▼] [All Priority ▼]│
│                                          │
│  ┌────────────────┬──────────────────┐  │
│  │  ➕ NEW TASK   │   MY TASKS       │  │
│  ├────────────────┼──────────────────┤  │
│  │                │                  │  │
│  │ Title: [____]  │ ┌──────────────┐ │  │
│  │                │ │Task 1   🔴HIGH│ │  │
│  │ Desc: [____]   │ │Status: DOING  │ │  │
│  │                │ │[Edit] [Delete]│ │  │
│  │ Priority:      │ └──────────────┘ │  │
│  │ [Medium ▼]     │                  │  │
│  │                │ ┌──────────────┐ │  │
│  │ Status:        │ │Task 2  🟡MED │ │  │
│  │ [Todo ▼]       │ │Status: TODO   │ │  │
│  │                │ │[Edit] [Delete]│ │  │
│  │ Deadline:      │ └──────────────┘ │  │
│  │ [📅 Pick]      │                  │  │
│  │                │                  │  │
│  │ [CREATE TASK]  │                  │  │
│  └────────────────┴──────────────────┘  │
└──────────────────────────────────────────┘
```

### Sektion 6: SPRINT BOARD (Kanban)
```
┌──────────┬──────────┬──────────┬──────────┐
│  TODO    │  DOING   │ REVIEW   │   DONE   │
├──────────┼──────────┼──────────┼──────────┤
│          │          │          │          │
│ □ AI     │ ⚙ Design│          │ ✓ Setup  │
│   Suggest│   TaskCard│         │   repo   │
│          │          │          │          │
│ □ Deploy │ ⚙ API    │          │ ✓ DB     │
│   Render │   CRUD   │          │   setup  │
│          │          │          │          │
│ □ Email  │          │          │ ✓ Models │
│   notify │          │          │          │
│          │          │          │          │
└──────────┴──────────┴──────────┴──────────┘
```

### Sektion 7: BESLUT & NOTES
```
Tekniska Beslut:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ PostgreSQL istället för SQLite
  → Mer realistiskt för produktion
  
✓ Tailwind CSS istället för CSS modules
  → Snabbare utveckling, konsekvent design
  
✓ Vite istället för Create React App
  → Modernare, snabbare build
  
? Authentication med JWT?
  → Beslut: Nej för MVP, kanske VG
  
? WebSockets för real-time?
  → Beslut: Nice-to-have, inte kritiskt

Challenges:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠ CORS-konfiguration mellan frontend/backend
  → Lösning: Korrekt middleware setup
  
⚠ Date/Time hantering mellan frontend/backend
  → Lösning: ISO 8601 format, UTC
  
⚠ State management när task uppdateras
  → Lösning: Fetch hela listan efter update
```

### Sektion 8: VG FEATURES (Brainstorm)
```
Möjliga VG-funktioner:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. AI Task Suggestions ⭐⭐⭐
   - OpenAI API integration
   - Generate subtasks
   - Smart prioritering
   
2. Async Email Notifications ⭐⭐⭐
   - Background tasks
   - Deadline reminders
   - Daily digest
   
3. Redis Caching ⭐⭐
   - Cache task lists
   - Performance improvement
   - Cache invalidation strategy
   
4. Advanced Analytics ⭐⭐
   - Productivity metrics
   - Time tracking
   - Completion rate över tid
   
5. Export Functionality ⭐
   - JSON export
   - CSV export
   - Backup data
   
6. Deployment ⭐⭐⭐
   - Render/Railway (backend)
   - Vercel/Netlify (frontend)
   - Environment variables
   
Väljer: #1, #2, #6 (Strong VG)
```

## Tips för Miro-arbete

1. **Använd färger**: Olika färger för olika typer av cards
   - Grönt = Klart
   - Gult = Pågående
   - Rött = Blockerare
   - Blått = Idéer

2. **Uppdatera dagligen**: Flytta cards mellan kolumner

3. **Screenshot för dokumentation**: Ta screenshots av boardens progress

4. **Använd sticky notes**: För snabba idéer och diskussioner

5. **Länka till koden**: Lägg till GitHub commit-länkar på cards

6. **Retrospective sektion**: Reflektera över vad som gick bra/dåligt

## Exempel Miro Flow

```
Vecka 1: Brainstorming → Wireframes → Tech Stack
Vecka 2: Sprint Planning → Daily standups på board
Vecka 3: Progress tracking → Bug tracking
Vecka 4: VG Feature planning → Testing notes
Vecka 5: Demo preparation → Reflection
```

---

**Pro tip**: Exportera Miro board som PDF för att bifoga i din slutliga redovisning!
