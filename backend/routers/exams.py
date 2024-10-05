from fastapi import APIRouter

router = APIRouter()

@router.get("/exams/", tags=["exams"])
def read_exams(): 
    return "these are all the exams"