from sqlalchemy.orm import Session
from . import models, schemas


def get_exams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Exam).offset(skip).limit(limit).all()


def create_exam(db: Session, exam: schemas.ExamCreate):
    db_exam = models.Exam(title=exam.title)

    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)

    return db_exam


def get_questions(db: Session, exam_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Question)
        .filter(models.Question.exam_id == exam_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_question(db: Session, exam_id: int, quesiton: schemas.QuestionCreate):
    db_question = models.Question(
        exam_id=exam_id, text=quesiton.text, answer=quesiton.answer
    )

    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    return db_question
