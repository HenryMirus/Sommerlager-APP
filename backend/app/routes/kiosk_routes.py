from fastapi import APIRouter

router = APIRouter()

@router.get("/snacks")
def list_snacks():
    return ["Chips", "Cola"]

@router.post("/orders")
def order_snack():
    return {"message": "Snack bestellt"}

