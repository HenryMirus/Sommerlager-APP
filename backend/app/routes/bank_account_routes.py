from fastapi import APIRouter

router = APIRouter()

@router.get("/accounts")
def list_accounts():
    return [{"user_id": 1, "balance": 20.0}]

@router.post("/accounts/{user_id}/deposit")
def deposit(user_id: int):
    return {"message": f"Einzahlung fuer User {user_id} erfolgreich"}
