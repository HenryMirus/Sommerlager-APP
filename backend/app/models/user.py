from sqlalchemy import Column, Integer, String, Boolean, Enum
from backend.app.database import Base
import enum

class UserRole(str, enum.Enum):
    KIND = "kind"
    BETREUER = "betreuer"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.KIND)
    is_active = Column(Boolean, default=True)
    # hier weiteere Attribute hinzufügen, bzw verlinkungen zu weiteren Dokumenten.
