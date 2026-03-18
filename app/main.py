from fastapi import FastAPI
from app.database import engine, Base
from app.models import user, restaurant # This is CRITICAL! 

# Tell SQLAlchemy to create the tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Uber Eats API is running!"}