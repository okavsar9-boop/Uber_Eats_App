from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user_schema import UserCreate, UserOut
from app.services import user_service

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    new_user = user_service.create_user(db, user_data)
    return new_user