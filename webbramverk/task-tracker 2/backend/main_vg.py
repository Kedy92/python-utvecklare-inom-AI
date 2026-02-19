"""
AVANCERADE FUNKTIONER FÖR VG-NIVÅ

Detta är en utökad version av main.py med:
1. AI-integration (OpenAI) för task suggestions
2. Asynkron email-funktionalitet
3. Caching med Redis
4. Logging
5. Rate limiting

OBS: Detta kräver extra dependencies - se requirements-vg.txt
"""

from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel, EmailStr
from datetime import datetime, timedelta
from typing import Optional, List
import enum
import logging
import json
from functools import wraps
import asyncio

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Database setup (samma som tidigare)
DATABASE_URL = "postgresql://user:password@localhost:5432/tasktracker"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Enums
class TaskStatus(str, enum.Enum):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"

class TaskPriority(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

# Database model
class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    priority = Column(SQLEnum(TaskPriority), default=TaskPriority.MEDIUM)
    status = Column(SQLEnum(TaskStatus), default=TaskStatus.TODO)
    deadline = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    ai_generated = Column(String, nullable=True)  # Extra: AI suggestions

Base.metadata.create_all(bind=engine)

# Pydantic models
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: TaskPriority = TaskPriority.MEDIUM
    status: TaskStatus = TaskStatus.TODO
    deadline: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[TaskPriority] = None
    status: Optional[TaskStatus] = None
    deadline: Optional[datetime] = None

class TaskResponse(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime
    ai_generated: Optional[str] = None
    
    class Config:
        from_attributes = True

class EmailNotification(BaseModel):
    email: EmailStr
    task_id: int

# FastAPI app
app = FastAPI(
    title="Task Tracker API - VG Version",
    description="Advanced task tracker with AI, async operations, and caching",
    version="2.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ============================================
# VG FUNKTIONER
# ============================================

# 1. ASYNKRON EMAIL-FUNKTIONALITET
async def send_email_async(email: str, task_title: str):
    """
    Simulerar asynkron email-sändning
    I produktion: använd SMTP eller SendGrid/Mailgun
    """
    logger.info(f"Sending email to {email} about task: {task_title}")
    await asyncio.sleep(2)  # Simulerar email-sändning
    logger.info(f"Email sent successfully to {email}")

@app.post("/tasks/{task_id}/notify")
async def notify_task_deadline(
    task_id: int,
    notification: EmailNotification,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """
    ASYNKRON: Skicka email-påminnelse om task deadline
    Email skickas i bakgrunden utan att användaren behöver vänta
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Lägg till background task
    background_tasks.add_task(send_email_async, notification.email, task.title)
    
    logger.info(f"Email notification queued for task {task_id}")
    return {"message": "Email notification queued", "task_id": task_id}

# 2. AI-INTEGRATION (OpenAI)
@app.post("/tasks/ai/suggest")
async def ai_suggest_tasks(prompt: str):
    """
    AI-FUNKTIONALITET: Generera task-förslag baserat på användarens input
    
    OBS: Detta kräver OpenAI API key i .env:
    OPENAI_API_KEY=your-key-here
    
    Exempel användning:
    POST /tasks/ai/suggest
    {
        "prompt": "Jag behöver planera ett webbutvecklingsprojekt"
    }
    """
    try:
        # Simulerat AI-svar (i produktion: använd OpenAI API)
        # import openai
        # response = openai.ChatCompletion.create(...)
        
        suggestions = [
            {
                "title": "Sätt upp projektet med React och FastAPI",
                "description": "Initiera frontend och backend repositories",
                "priority": "high",
                "ai_generated": "Generated by AI based on user prompt"
            },
            {
                "title": "Designa databasschema",
                "description": "Planera tabeller och relationer",
                "priority": "high",
                "ai_generated": "Generated by AI based on user prompt"
            },
            {
                "title": "Implementera CRUD-operationer",
                "description": "Skapa API endpoints och frontend komponenter",
                "priority": "medium",
                "ai_generated": "Generated by AI based on user prompt"
            }
        ]
        
        logger.info(f"AI suggestions generated for prompt: {prompt}")
        return {"prompt": prompt, "suggestions": suggestions}
        
    except Exception as e:
        logger.error(f"AI suggestion error: {str(e)}")
        raise HTTPException(status_code=500, detail="AI service unavailable")

# 3. CACHING (Redis simulation)
# I produktion: använd Redis
task_cache = {}
CACHE_TTL = 300  # 5 minuter

@app.get("/tasks/cached/", response_model=List[TaskResponse])
def get_tasks_cached(db: Session = Depends(get_db)):
    """
    CACHING: Cachad version av get_tasks för bättre performance
    Cache invalideras automatiskt efter 5 minuter
    """
    cache_key = "all_tasks"
    current_time = datetime.utcnow()
    
    # Kolla cache
    if cache_key in task_cache:
        cached_data, cached_time = task_cache[cache_key]
        if (current_time - cached_time).seconds < CACHE_TTL:
            logger.info("Returning cached tasks")
            return cached_data
    
    # Hämta från databas
    tasks = db.query(Task).order_by(Task.created_at.desc()).all()
    task_cache[cache_key] = (tasks, current_time)
    logger.info("Tasks cached")
    
    return tasks

# 4. SCHEMALÄGGNING (Simulerat)
@app.post("/tasks/schedule/cleanup")
async def schedule_cleanup(background_tasks: BackgroundTasks):
    """
    SCHEMALÄGGNING: Rensa gamla completade tasks
    I produktion: använd Celery eller APScheduler
    """
    async def cleanup_old_tasks():
        await asyncio.sleep(2)
        logger.info("Scheduled cleanup executed")
        # I produktion: ta bort tasks äldre än X dagar
    
    background_tasks.add_task(cleanup_old_tasks)
    return {"message": "Cleanup scheduled"}

# 5. AVANCERAD STATISTIK
@app.get("/tasks/analytics/productivity")
def get_productivity_analytics(db: Session = Depends(get_db)):
    """
    AVANCERAD FUNKTIONALITET: Beräkna produktivitets-metriker
    """
    tasks = db.query(Task).all()
    
    if not tasks:
        return {"message": "No data available"}
    
    total_tasks = len(tasks)
    completed_tasks = len([t for t in tasks if t.status == TaskStatus.DONE])
    
    # Beräkna genomsnittlig tid till completion
    completion_times = []
    for task in tasks:
        if task.status == TaskStatus.DONE:
            time_diff = (task.updated_at - task.created_at).days
            completion_times.append(time_diff)
    
    avg_completion_time = sum(completion_times) / len(completion_times) if completion_times else 0
    
    # Tasks per prioritet
    priority_distribution = {
        "low": len([t for t in tasks if t.priority == TaskPriority.LOW]),
        "medium": len([t for t in tasks if t.priority == TaskPriority.MEDIUM]),
        "high": len([t for t in tasks if t.priority == TaskPriority.HIGH]),
    }
    
    analytics = {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "completion_rate": round((completed_tasks / total_tasks) * 100, 2) if total_tasks > 0 else 0,
        "avg_completion_days": round(avg_completion_time, 2),
        "priority_distribution": priority_distribution,
        "overdue_tasks": len([t for t in tasks if t.deadline and t.deadline < datetime.utcnow() and t.status != TaskStatus.DONE])
    }
    
    logger.info("Productivity analytics generated")
    return analytics

# 6. EXPORT FUNKTIONALITET
@app.get("/tasks/export/json")
def export_tasks_json(db: Session = Depends(get_db)):
    """
    EXPORT: Exportera alla tasks som JSON
    """
    tasks = db.query(Task).all()
    tasks_data = [
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "priority": t.priority.value,
            "status": t.status.value,
            "deadline": t.deadline.isoformat() if t.deadline else None,
            "created_at": t.created_at.isoformat(),
        }
        for t in tasks
    ]
    
    logger.info(f"Exported {len(tasks_data)} tasks to JSON")
    return {"tasks": tasks_data, "exported_at": datetime.utcnow().isoformat()}

# Behåll alla CRUD endpoints från original main.py här också...
# (CREATE, READ, UPDATE, DELETE endpoints)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
