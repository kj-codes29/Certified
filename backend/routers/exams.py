from typing import Annotated, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..data import database, schemas
from ..data.respository import exam_repository as repository

SessionDep = Annotated[Session, Depends(database.get_db)]

router = APIRouter(prefix="/exams", tags=["exams"])


@router.get("/", response_model=List[schemas.Exam])
def get_all_exams(db: SessionDep):
    return repository.get_exams(db)


@router.post("/", response_model=schemas.Exam)
def create_exam(exam: schemas.ExamBase, db: SessionDep):
    return repository.create_exam(db, exam)

@router.put("/{exam_id}", response_model=schemas.Exam)
def update_exam(exam_id: int, exam: schemas.ExamBase, db: SessionDep):
    return repository.update_exam(db, exam_id, exam)


@router.delete("/{exam_id}", response_model=schemas.Exam)
def delete_exam(exam_id: int, db: SessionDep):
    return repository.delete_exam(db, exam_id)