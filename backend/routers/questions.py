from fastapi import APIRouter

router = APIRouter()

@router.get("/questions/", tags=["questions"])
def read_questions(): 
    return "these are all the questions"