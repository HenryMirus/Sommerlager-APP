# app/routes/auth_routes.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # TODO: Implementiere Authentifizierung
    return {"access_token": "mock_token", "token_type": "bearer"}

