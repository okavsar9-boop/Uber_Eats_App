from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user_schema import UserOut, UserCreate
# Import your new dependency here
from app.dependencies import get_current_user 

router = APIRouter(prefix="/users", tags=["Users"])

# ... (Keep your register and login routes here)

@router.get("/me", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
    """
    This route is PROTECTED. If you don't provide a valid JWT token,
    FastAPI will automatically return a 401 Unauthorized error.
    """
    return current_user