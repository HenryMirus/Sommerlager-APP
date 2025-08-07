from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.user_schema import UserCreate, UserOut
from ..services import user_service

router = APIRouter()

@router.get("/", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")
    return user

@router.post("/", response_model=UserOut)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    existing = user_service.get_user_by_username(user_data.username, db)
    if existing:
        raise HTTPException(status_code=400, detail="Username existiert bereits")
    return user_service.create_user(user_data, db)

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = user_service.delete_user(user_id, db)
    if not deleted:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")
