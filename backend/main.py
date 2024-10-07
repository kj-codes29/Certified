from typing import Union
from fastapi import FastAPI
from .data.database import Base, engine
from .routers import exams, questions

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(exams.router)
app.include_router(questions.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
