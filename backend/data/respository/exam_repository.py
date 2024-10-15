from sqlalchemy.orm import Session
from .. import models, schemas


def get_exams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Exam).offset(skip).limit(limit).all()


def create_exam(db: Session, exam: schemas.ExamBase):
    db_exam = models.Exam(title=exam.title)

    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)

    return db_exam

def update_exam(db: Session, exam_id: int, exam: schemas.ExamBase):
    db_exam = db.query(models.Exam).filter(models.Exam.id == exam_id).first()

    db_exam.title = exam.title

    db.commit()
    db.refresh(db_exam)

    return db_exam

def delete_exam(db: Session, exam_id: int):
    db_exam = db.query(models.Exam).filter(models.Exam.id == exam_id).first()

    db.delete(db_exam)
    db.commit()

    return db_exam