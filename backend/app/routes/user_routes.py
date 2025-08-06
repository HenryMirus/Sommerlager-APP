from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/")
def list_users():
    return ["user1", "user2"]

@router.post("/")
def create_user():
    return {"message": "Benutzer erstellt"}
