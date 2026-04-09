from pydantic import BaseModel
from typing import Optional

class RestaurantBase(BaseModel):
    name: str
    address_line: str
    city: str
    postal_code: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class RestaurantCreate(RestaurantBase):
    pass # Data required to create a restaurant

class RestaurantOut(RestaurantBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True