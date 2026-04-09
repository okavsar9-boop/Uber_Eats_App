from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import verify_password, create_access_token

# Add this to your user_routes.py
@router.post("/login")
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    # 1. Find the user by email
    user = db.query(user.User).filter(user.User.email == form_data.username).first()
    
    # 2. Check if user exists and password is correct
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    # 3. Create the "Digital ID Card" (Token)
    access_token = create_access_token(data={"sub": user.email, "role": user.role})
    
    return {"access_token": access_token, "token_type": "bearer"}