from sqlalchemy.orm import Session
from .. import models, schemas

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