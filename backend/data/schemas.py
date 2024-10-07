from typing import List
from pydantic import BaseModel


class QuestionBase(BaseModel):
    text: str
    answer: str


class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    id: int
    exam_id: int

    class Config:
        orm_mode = True


class ExamBase(BaseModel):
    title: str


class ExamCreate(ExamBase):
    questions: List[QuestionCreate] = []


class Exam(ExamBase):
    id: int
    questions: List[QuestionCreate] = []

    class Config:
        orm_mode = True
