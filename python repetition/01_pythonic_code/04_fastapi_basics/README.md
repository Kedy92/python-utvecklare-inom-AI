# FastAPI Basics

## Setup

```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

## Structure

- `main.py` - FastAPI application and endpoints
- `database.py` - SQLite database functions
- `models.py` - Pydantic models for validation
- `exceptions.py` - Custom exceptions

## Key Concepts

- Error handling in real API context
- Helper functions that raise exceptions
- Pydantic for input validation
- HTTPException for proper error responses
