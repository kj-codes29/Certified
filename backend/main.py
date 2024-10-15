
from fastapi import FastAPI
from .data.database import create_db_and_tables
from .routers import exams, questions

create_db_and_tables()

app = FastAPI()

app.include_router(exams.router)
app.include_router(questions.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
