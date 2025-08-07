from pydantic import BaseModel
from enum import Enum

class UserRole(str, Enum):
    KIND = "kind"
    BETREUER = "betreuer"
    ADMIN = "admin"

class UserBase(BaseModel):
    name: str
    username: str
    role: UserRole = UserRole.KIND

class UserCreate(UserBase):
    password: str  # Nur beim Erstellen

class UserOut(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
