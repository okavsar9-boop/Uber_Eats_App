import enum
from sqlalchemy import Column, Integer, String, TIMESTAMP, Enum, func
from app.database import Base

# This acts as a 'whitelist' for roles
class UserRole(str, enum.Enum):
    CUSTOMER = "customer"
    COURIER = "courier"
    RESTAURANT = "restaurant"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    # This enforces that only the three roles above are allowed
    role = Column(Enum(UserRole), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())