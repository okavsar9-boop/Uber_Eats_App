from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate

def create_user(db: Session, user_data: UserCreate):
    # In a real app, we would hash the password here!
    new_user = User(
        email=user_data.email,
        password=user_data.password, # We will add hashing in the next step
        role=user_data.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user