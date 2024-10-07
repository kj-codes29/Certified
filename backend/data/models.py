from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from backend.data.database import Base


class Exam(Base):
    __tablename__ = "exam"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)

    questions = relationship(
        "Question", back_populates="exam", cascade="all, delete-orphan"
    )


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    answer = Column(String)

    exam_id = Column(Integer, ForeignKey("exam.id"))

    exam = relationship("Exam", back_populates="questions")
