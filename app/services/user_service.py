from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.core.security import hash_password # Import the tool

def create_user(db: Session, user_data: UserCreate):
    # Hash the password! 
    hashed_pwd = hash_password(user_data.password)
    
    new_user = User(
        email=user_data.email,
        password=hashed_pwd, # Save the "scrambled" version
        role=user_data.role
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user