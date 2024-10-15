from typing import Annotated, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..data import database, schemas
from ..data.respository import question_repository as repository

SessionDep = Annotated[Session, Depends(database.get_db)]

router = APIRouter(prefix="/questions", tags=["questions"])


@router.get("/{exam_id}", response_model=List[schemas.Question])
def get_all_questions(exam_id: int, db: SessionDep):
    return repository.get_questions(db, exam_id)


@router.post("/{exam_id}", response_model=schemas.Question)
def add_questions_with_file(
    exam_id: int,
    question: schemas.QuestionBase,
    db: SessionDep,
):
    return repository.create_question(db, exam_id, question)


@router.put("/{question_id}", response_model=schemas.Question)
def update_question(
    quesiton_id: int,
    question: schemas.QuestionBase,
    db: SessionDep,
):
    return repository.update_question(db, question, quesiton_id)


@router.delete("/{question_id}", response_model=schemas.QuestionBase)
def delete_question(question_id: int, db: SessionDep):
    return repository.delete_question(db, question_id)
