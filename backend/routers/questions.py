from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..data import database, schemas
from ..data.respository import exam_repository as repository


router = APIRouter(prefix="/questions", tags=["questions"])


@router.get("/{exam_id}", response_model=List[schemas.Question])
def get_all_questions(exam_id: int, db: Session = Depends(database.get_db)):
    return repository.get_questions(db, exam_id)


@router.post("/{exam_id}", response_model=schemas.Question)
def add_questions_with_file(
    exam_id: int,
    question: schemas.QuestionCreate,
    db: Session = Depends(database.get_db),
):
    return repository.create_question(db, exam_id, question)
