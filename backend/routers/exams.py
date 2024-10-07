from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..data import database, schemas, crud


router = APIRouter(prefix="/exams", tags=["exams"])


@router.get("/", response_model=List[schemas.Exam])
def get_all_exams(db: Session = Depends(database.get_db)):
    return crud.get_exams(db)


@router.post("/", response_model=schemas.Exam)
def create_exam(exam: schemas.ExamCreate, db: Session = Depends(database.get_db)):
    return crud.create_exam(db, exam)
