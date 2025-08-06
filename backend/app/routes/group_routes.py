from fastapi import APIRouter

router = APIRouter()

@router.post("/auto")
def auto_generate_groups():
    return {"message": "Gruppen automatisch erstellt"}

