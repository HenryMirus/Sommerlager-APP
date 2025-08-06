from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def create_lager():
    return {"message": "Sommerlager erstellt"}

@router.get("/active")
def get_active_lager():
    return {"lager_id": 1, "status": "aktiv"}

