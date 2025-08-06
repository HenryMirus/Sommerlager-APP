from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_photos():
    return ["photo1.jpg", "photo2.jpg"]