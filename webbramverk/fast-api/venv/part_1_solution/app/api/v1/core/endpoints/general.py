from app.api.v1.core.models import Company
from app.api.v1.core.schemas import CompanySchema
from app.db_setup import get_db
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Request, status
from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import Session, joinedload, selectinload

router = APIRouter(tags=["dashboard"], prefix="/dashboard")


@router.get("/company", status_code=200)
def list_companies(db: Session = Depends(get_db)):
    programs = db.scalars(select(Company)).all()
    if not programs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No companies found"
        )
    return programs


@router.post("/company", status_code=201)
def add_company(company: CompanySchema, db: Session = Depends(get_db)) -> CompanySchema:
    db_company = Company(**company.model_dump())  # **data.dict() deprecated
    db.add(db_company)
    db.commit()
    db.refresh(db_company)  # Vi ser till att vi får den uppdaterade versionen med ID't
    # Du kan skippa .refresh() om du använt expire_on_commit=False i ditt sessionobjekt
    return db_company
