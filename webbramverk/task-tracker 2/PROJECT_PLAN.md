# Projektplan - Task Tracker

## Projekt Information
- **Projektnamn**: Task Tracker - Produktivitetsapplikation
- **Team**: [Ditt namn] & [Partners namn]
- **Startdatum**: 2025-02-01
- **Slutdatum**: 2025-03-15
- **Repository**: https://github.com/[username]/task-tracker

## Projektmål

Skapa en fullstack webbapplikation som hjälper användare att hantera och följa upp sina uppgifter med fokus på produktivitet och användarvänlighet.

## Veckoplan (Agil Sprint-struktur)

### Vecka 1: Setup & Grundläggande Backend
**Mål**: Få igång projekt-infrastruktur och grundläggande CRUD

- [ ] Sätt upp Git repository och bjud in läraren
- [ ] Konfigurera PostgreSQL databas
- [ ] Skapa FastAPI projekt med SQLAlchemy
- [ ] Implementera Task model
- [ ] Skapa CRUD endpoints (CREATE, READ)
- [ ] Testa endpoints i Swagger UI

**Daily standup frågor:**
1. Vad gjorde jag igår?
2. Vad ska jag göra idag?
3. Finns det några blockerare?

### Vecka 2: Slutför Backend & Börja Frontend
**Mål**: Komplett backend API och React setup

- [ ] Implementera UPDATE och DELETE endpoints
- [ ] Lägg till filtrering och sortering
- [ ] Skapa statistik endpoint
- [ ] Sätt upp React projekt med Vite
- [ ] Konfigurera Tailwind CSS
- [ ] Skapa grundläggande komponenter (TaskForm, TaskList)

### Vecka 3: Frontend Integration & Design
**Mål**: Anslut frontend till backend och polera design

- [ ] Implementera API-anrop i React
- [ ] Skapa alla komponenter (TaskCard, TaskStats, FilterBar)
- [ ] Implementera state management
- [ ] Design med Tailwind CSS
- [ ] Responsiv layout
- [ ] Error handling

### Vecka 4: VG-funktioner & Testing
**Mål**: Lägg till avancerad funktionalitet

Välj 2-3 av följande:
- [ ] AI-integration för task suggestions
- [ ] Asynkron email-funktionalitet
- [ ] Caching med Redis
- [ ] Export till JSON/CSV
- [ ] Avancerad analytics
- [ ] Deployment (Render + Vercel)

### Vecka 5: Polish & Förberedelse för Redovisning
**Mål**: Slutför projektet och förbered demo

- [ ] Bugfixing
- [ ] Koda-granskning
- [ ] Dokumentation (README, kommentarer)
- [ ] Förbereda demo
- [ ] Testa alla funktioner
- [ ] Skapa presentation

## Arbetsfördelning

### Person 1: [Namn]
**Huvudansvar:**
- Backend utveckling (FastAPI, SQLAlchemy)
- Databas design och migration
- API dokumentation
- VG-funktioner (Backend-fokus)

**Komponenter:**
- main.py endpoints
- Database models
- Pydantic schemas
- Background tasks

### Person 2: [Namn]
**Huvudansvar:**
- Frontend utveckling (React)
- UI/UX design
- State management
- VG-funktioner (Frontend-fokus)

**Komponenter:**
- TaskForm, TaskList, TaskCard
- App.jsx (main logic)
- Styling med Tailwind
- API integration

## Tekniska Beslut

### Backend
- **Framework**: FastAPI (modernt, snabbt, bra docs)
- **ORM**: SQLAlchemy (industry standard)
- **Database**: PostgreSQL (robust, skalbar)
- **Validation**: Pydantic (inbyggt i FastAPI)

### Frontend
- **Framework**: React (populärt, stort community)
- **Build Tool**: Vite (snabbt, modernt)
- **Styling**: Tailwind CSS (snabb utveckling, konsekvent design)
- **HTTP Client**: Fetch API (native, inget extra library)

### Deployment (VG)
- **Backend**: Render / Railway
- **Frontend**: Vercel / Netlify
- **Database**: Render PostgreSQL

## Git Workflow

### Branch Strategy
```
main (production-ready kod)
  └── develop (utveckling)
       ├── feature/task-form
       ├── feature/task-list
       ├── feature/ai-integration
       └── bugfix/filter-not-working
```

### Commit Konvention
```
feat: Ny funktionalitet
fix: Buggfix
docs: Dokumentation
style: Formatering
refactor: Kod-omstrukturering
test: Tester
chore: Underhåll
```

**Exempel:**
```bash
git commit -m "feat: Add task filtering by priority"
git commit -m "fix: Resolve deadline date formatting issue"
git commit -m "docs: Update README with setup instructions"
```

### Daily Git Rutiner
1. Starta dagen: `git pull origin develop`
2. Skapa feature branch: `git checkout -b feature/[namn]`
3. Commit regelbundet (minst 3-5 commits/dag)
4. Push dagligen: `git push origin feature/[namn]`
5. Merge när klar: Pull request → Code review → Merge

## Kvalitetssäkring

### Code Review Checklist
- [ ] Koden följer projektets stil-guide
- [ ] Funktionalitet fungerar som förväntat
- [ ] Inga console.log() eller debug-kod kvar
- [ ] Kommentarer där nödvändigt (ej överflödigt)
- [ ] Error handling implementerad
- [ ] Responsiv design funkar på mobil/tablet/desktop

### Testing Checklist
- [ ] Alla CRUD-operationer fungerar
- [ ] Filtrering och sortering funkar
- [ ] Formulär-validering fungerar
- [ ] Error messages visas korrekt
- [ ] Statistik uppdateras korrekt
- [ ] Deadline-varningar visas rätt

## Risker & Mitigering

| Risk | Sannolikhet | Impact | Mitigering |
|------|-------------|--------|------------|
| Databas-anslutning problem | Medium | Hög | Testa lokalt först, använd .env korrekt |
| CORS-problem | Hög | Medium | Konfigurera CORS rätt från start |
| Merge conflicts | Medium | Medium | Kommunicera, daily syncs |
| Tidsbrist för VG | Medium | Medium | Prioritera kärnfunktionalitet först |
| En teammedlem blir sjuk | Låg | Hög | Dokumentera väl, pair programming |

## Success Metrics

### Godkänd-nivå (Minimum)
✅ Full CRUD-funktionalitet
✅ Working frontend i React
✅ Working backend i FastAPI
✅ PostgreSQL databas
✅ Professionell design
✅ Bra commit-historik

### VG-nivå (Mål)
✅ 2-3 avancerade features implementerade
✅ Deployment (backend + frontend)
✅ Tydlig värdeskapande idé
✅ Stark förståelse för kodbas
✅ God kodkvalitet och struktur
✅ Utmärkt demo presentation

## Resurser

### Dokumentation
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [React Docs](https://react.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)

### Lärresurser
- FastAPI Tutorial: [YouTube Playlist]
- React Hooks: [React Official Tutorial]
- PostgreSQL: [PostgreSQL Tutorial]

## Kontakt & Kommunikation

- **Daily Standups**: Varje morgon 09:00
- **Code Reviews**: Efter varje större feature
- **Team Sync**: Fredag eftermiddag (veckosammanfattning)
- **Kommunikation**: Discord / Slack
- **Screen Sharing**: När behövs för pair programming

## Veckoavstämningar med Lärare

### Vecka 1 Avstämning
- Visa setup (databas, repo, basic endpoints)
- Diskutera arkitektur-beslut

### Vecka 2 Avstämning  
- Demo av CRUD-funktionalitet
- Visa frontend progress

### Vecka 3 Avstämning
- Fullständig demo av grundfunktionalitet
- Diskutera VG-planer

---

**Uppdateras kontinuerligt under projektets gång!**
