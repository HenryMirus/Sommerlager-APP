from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user_schema import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_id(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(username: str, db: Session):
    return db.query(User).filter(User.username == username).first()

def create_user(user_data: UserCreate, db: Session):
    hashed_pw = pwd_context.hash(user_data.password)
    new_user = User(
        name=user_data.name,
        username=user_data.username,
        role=user_data.role,
        hashed_password=hashed_pw
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def delete_user(user_id: int, db: Session):
    user = get_user_by_id(user_id, db)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
