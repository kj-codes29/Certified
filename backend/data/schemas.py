from typing import List
from pydantic import BaseModel


class QuestionBase(BaseModel):
    text: str
    answer: str

class Question(QuestionBase):
    id: int
    exam_id: int

    class Config:
        orm_mode = True


class Question(QuestionBase):
    id: int
    exam_id: int

    class Config:
        orm_mode = True


class ExamBase(BaseModel):
    title: str

class Exam(ExamBase):
    id: int
    questions: List[QuestionBase] = []

    class Config:
        orm_mode = True
