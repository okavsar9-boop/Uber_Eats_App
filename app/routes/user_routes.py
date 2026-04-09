from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.restaurant_schema import RestaurantCreate, RestaurantOut
from app.services import restaurant_service
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])

@router.post("/", response_model=RestaurantOut, status_code=status.HTTP_201_CREATED)
def add_restaurant(
    restaurant_data: RestaurantCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    # This ensures the restaurant is linked to the person who is logged in!
    return restaurant_service.create_restaurant(db, restaurant_data, current_user.id)