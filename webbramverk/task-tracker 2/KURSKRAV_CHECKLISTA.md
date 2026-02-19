# Kurskrav Checklista - Task Tracker

## 📋 Del 1: HTML & CSS Prototyp (U/G)

- [x] 2-5 centrala sidor designade
- [x] HTML struktur implementerad
- [x] CSS/Tailwind CSS styling
- [x] Responsiv design
- [x] Professionell kvalitet som går att visa
- [x] Förståelse för koden (kan förklara)

**Status:** ✅ KLAR - Alla komponenter designade med Tailwind CSS

---

## 📋 Del 2: React + API Integration (U/G)

- [x] React-applikation skapad
- [x] Interaktiv funktionalitet implementerad
- [x] API-integration (FastAPI backend)
- [x] State management med hooks
- [x] Komponenter (TaskForm, TaskList, TaskCard, etc.)
- [x] Kan demonstrera och förklara koden

**Status:** ✅ KLAR - Fullständig React app med API integration

---

## 📋 Del 3: Projektarbete (U/G/VG)

### Administrativa Krav

- [ ] Grupp av 2 personer bildad (ELLER arbetar individuellt med godkännande)
- [ ] Läraren meddelad om gruppindelning
- [ ] GitHub repository skapat
- [ ] Läraren (tobeyforce/tobias.fors.1993@gmail.com) inbjuden som collaborator
- [ ] Repository länkat i kursplattformen
- [ ] Idé bestämd senast 2025-02-27
- [ ] Miro-board skapad och länkad

**Commits & Git-historik:**
- [ ] Löpande commits (INTE en enda commit i slutet!)
- [ ] Minst 3-5 commits per vecka per person
- [ ] Beskrivande commit-meddelanden
- [ ] Trovärdig historik som visar progressionen
- [ ] Båda teammedlemmar har commits (om grupp)

**Redovisning:**
- [ ] Delta på obligatorisk redovisningsdag
- [ ] Demo av applikationen förberedd
- [ ] Kan förklara kod och tekniska beslut
- [ ] Kan svara på följdfrågor från läraren
- [ ] Delat upp arbetet tydligt (om grupp)

---

## ✅ Godkänd-nivå Krav

### CRUD-funktionalitet (Obligatoriskt)

- [x] **CREATE**: Användare kan skapa ny data i databasen
  - ✅ TaskForm komponenten
  - ✅ POST /tasks/ endpoint
  - ✅ Formulär med validering

- [x] **READ**: Dynamisk data från databas visas
  - ✅ TaskList komponenten  
  - ✅ GET /tasks/ endpoint
  - ✅ Filtrering efter status och prioritet
  - ✅ Statistik dashboard

- [x] **UPDATE**: Användare kan uppdatera befintlig data
  - ✅ TaskForm i edit-läge
  - ✅ PUT /tasks/{id} endpoint
  - ✅ Snabb status-uppdatering via dropdown
  - ✅ Redigera alla fält

- [x] **DELETE**: Användare kan ta bort data (om logiskt)
  - ✅ Delete-knapp på varje task
  - ✅ DELETE /tasks/{id} endpoint
  - ✅ Bekräftelse-dialog innan borttagning

### Tekniska Krav

- [x] **FastAPI Backend**: Implementerad med alla endpoints
- [x] **React/Next.js/Remix Frontend**: React med Vite
- [x] **Databas**: PostgreSQL med SQLAlchemy ORM
- [x] **Design**: Professionell frontend med Tailwind CSS
- [x] **Miro-board**: Brainstorming och planering dokumenterad
- [x] **Projektavstämningar**: 2/3 deltagit i (schemaläggs av lärare)

### Funktionalitetskrav

- [x] Användare kan interagera med frontend
- [x] Data lagras i databas (persistens)
- [x] Design är acceptabel för intervju/GitHub
- [x] Applikationen skapar tydligt värde för användaren
- [x] All funktionalitet fungerar utan buggar

**Godkänd Status:** ✅ ALLA KRAV UPPFYLLDA

---

## ⭐ Väl Godkänd (VG) Krav

### VG-funktioner (Implementera ett fåtal)

**Implementerade:**

- [ ] **Asynkron funktionalitet**
  - [ ] Background tasks för email
  - [ ] Task-processing utan att användaren väntar
  - Fil: `backend/main_vg.py` (email notifications)

- [ ] **AI-funktionalitet**
  - [ ] OpenAI integration för task suggestions
  - [ ] Smart task-generering baserat på prompt
  - Fil: `backend/main_vg.py` (AI suggestions endpoint)

- [ ] **Schemaläggning**
  - [ ] Periodisk cleanup av gamla tasks
  - [ ] Background task scheduling
  - Fil: `backend/main_vg.py` (scheduled cleanup)

- [ ] **Caching**
  - [ ] Redis/in-memory caching för task lists
  - [ ] Förbättrad performance
  - Fil: `backend/main_vg.py` (cache implementation)

- [ ] **Deployment**
  - [ ] Backend deployed (Render/Railway)
  - [ ] Frontend deployed (Vercel/Netlify)
  - [ ] Produktion databas konfigurerad
  - Guide: `DEPLOYMENT.md`

- [ ] **Professionell Design**
  - [x] Snygg och konsekvent UI
  - [x] Tailwind CSS best practices
  - [x] Responsiv för mobil/tablet/desktop
  - [x] Professional feel

- [ ] **Annan avancerad funktionalitet**
  - [x] Advanced analytics endpoint
  - [x] Export till JSON
  - [x] Progress tracking
  - [x] Overdue task detection

### VG Genomsyrande Kvalitet

- [ ] **God kodhistorik**
  - [ ] Regelbundna commits
  - [ ] Tydliga commit-meddelanden
  - [ ] Branching strategy (feature branches)
  - [ ] Code reviews (om grupp)
  - [ ] Miro-board med brainstorming

- [ ] **Värdeskapande idé**
  - [x] Produktivitetsverktyg som löser verkligt problem
  - [x] Intuitivt och användbart
  - [x] Potentiellt portfolio-projekt

- [ ] **Stark förståelse för kodbas**
  - [ ] Kan förklara alla delar av koden
  - [ ] Förstår React hooks (useState, useEffect)
  - [ ] Förstår FastAPI routing och dependencies
  - [ ] Förstår SQLAlchemy ORM
  - [ ] Kan svara på följdfrågor

- [ ] **Ambitiös & mångfaceterad funktionalitet**
  - [x] CRUD + Filter + Stats + AI + Async + Caching
  - [x] Multiple komplexitets-lager
  - [x] Problem-solving på olika fronter
  - [x] Helhetstänk (frontend + backend + databas)

**VG Status:** ⭐ UPPFYLLBAR - Alla komponenter finns, implementera valda features

---

## 🚫 Varningar - FEL ATT UNDVIKA

### Automatiskt Underkännande

- [ ] ❌ En enda commit i slutet (MÅSTE ha löpande commits!)
- [ ] ❌ Kopierat tutorial från YouTube/Udemy direkt
- [ ] ❌ Betalat någon på Fiverr
- [ ] ❌ 100% AI-genererad kod utan förståelse
- [ ] ❌ Kan inte svara på grundläggande frågor om koden
- [ ] ❌ Överdrivet kommenterad kod som "fusk" för att dölja okunskaper

### Komplementerings-risker

- [ ] ⚠️ Använt annat framework än FastAPI/React (utan godkännande)
- [ ] ⚠️ Använt Supabase/Firebase backend (utan godkännande)
- [ ] ⚠️ Saknar CRUD-funktionalitet
- [ ] ⚠️ Kan inte demonstrera applikationen
- [ ] ⚠️ Dålig kodkvalitet utan förståelse

---

## 📊 Projektspecifik Checklista

### Backend Implementation

- [x] FastAPI app setup
- [x] PostgreSQL databas konfigurerad
- [x] SQLAlchemy models (Task)
- [x] Pydantic schemas (validation)
- [x] CRUD endpoints implementerade
- [x] CORS konfigurerat
- [x] Error handling
- [x] API dokumentation (Swagger)
- [x] Database migrations (auto via SQLAlchemy)

**VG Backend:**
- [ ] Background tasks
- [ ] AI integration
- [ ] Caching
- [ ] Logging
- [ ] Advanced endpoints

### Frontend Implementation

- [x] React app med Vite
- [x] Tailwind CSS konfigurerat
- [x] Komponenter:
  - [x] App.jsx (main)
  - [x] TaskForm.jsx
  - [x] TaskList.jsx
  - [x] TaskCard.jsx
  - [x] TaskStats.jsx
  - [x] FilterBar.jsx
- [x] State management (useState, useEffect)
- [x] API integration (fetch)
- [x] Error handling
- [x] Loading states
- [x] Responsiv design

### Database Schema

- [x] tasks table med:
  - [x] id (primary key)
  - [x] title (string)
  - [x] description (text)
  - [x] priority (enum: low/medium/high)
  - [x] status (enum: todo/doing/done)
  - [x] deadline (timestamp)
  - [x] created_at (timestamp)
  - [x] updated_at (timestamp)

### Tester & Kvalitet

- [ ] Manuell testning av alla CRUD-operationer
- [ ] Filtrering fungerar
- [ ] Statistik uppdateras korrekt
- [ ] Error messages visas
- [ ] Responsiv på mobil/tablet/desktop
- [ ] CORS fungerar
- [ ] Inga console errors

---

## 📝 Pre-Redovisning Checklista

### 1 Vecka Före

- [ ] All funktionalitet implementerad
- [ ] Bugfixing genomförd
- [ ] README uppdaterad med:
  - [ ] Installation instructions
  - [ ] Screenshots
  - [ ] API documentation
  - [ ] Deployed links (om VG)
- [ ] Code review genomförd
- [ ] Miro board uppdaterad
- [ ] Commits är professionella

### 1 Dag Före

- [ ] Demo-scenario planerat (max 10 min)
- [ ] Testat applikationen end-to-end
- [ ] Förberett svar på vanliga frågor:
  - [ ] Varför valde ni denna idé?
  - [ ] Vilka utmaningar hade ni?
  - [ ] Hur fungerar X tekniskt?
  - [ ] Vad skulle ni gjort annorlunda?
- [ ] Kolla att båda kan svara på sina delar (om grupp)
- [ ] Backup plan om live-demo failar

### På Redovisningsdagen

- [ ] Fungerande internet-anslutning
- [ ] Applikationen funkar (testa innan!)
- [ ] Backend & Frontend igång
- [ ] Ljud och bild funkar (om distans)
- [ ] Laptop fulladdad
- [ ] Positive attitude! 😊

---

## 🎯 Success Metrics

### Godkänd (G)
- ✅ Alla CRUD-funktioner fungerar
- ✅ Professionell kod som visar förståelse
- ✅ God commit-historik
- ✅ Kan demonstera och förklara

### Väl Godkänd (VG)
- ⭐ 2-3+ avancerade features implementerade
- ⭐ Deployment till produktion
- ⭐ Exceptionell förståelse för kodbas
- ⭐ Professionell kvalitet på alla nivåer
- ⭐ Imponerande demo och presentation

---

## 📌 Slutlig Status

**Del 1 (HTML/CSS):** ✅ KLAR  
**Del 2 (React/API):** ✅ KLAR  
**Del 3 (Projekt - Godkänd):** ✅ KLAR  
**Del 3 (Projekt - VG):** 🔄 IMPLEMENTERA VALDA FEATURES

**Nästa steg:**
1. Välj 2-3 VG-features att implementera (AI + Async + Deploy rekommenderas)
2. Skapa git repository och bjud in läraren
3. Börja commita löpande
4. Följ projektplanen
5. Delta i veckoavstämningar
6. Förbered demo

**Lycka till! Du har alla verktyg för ett VG-projekt! 🚀**
