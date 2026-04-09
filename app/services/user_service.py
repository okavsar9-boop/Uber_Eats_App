from sqlalchemy.orm import Session
from app.models.restaurant import Restaurant
from app.schemas.restaurant_schema import RestaurantCreate

def create_restaurant(db: Session, restaurant_data: RestaurantCreate, owner_id: int):
    new_restaurant = Restaurant(
        **restaurant_data.dict(), # This spreads out name, address, etc.
        owner_id=owner_id
    )
    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)
    return new_restaurant