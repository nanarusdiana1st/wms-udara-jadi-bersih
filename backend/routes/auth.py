from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import User
from ..schemas import UserCreate
from ..auth import get_password_hash, create_access_token, get_current_user
from typing import Annotated

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login")
async def login(user_data: UserCreate, db: Session = Depends(SessionLocal)):
    db_user = db.query(User).filter(User.username == user_data.username).first()
    if not db_user or not verify_password(user_data.password, db_user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register")
async def register(user_data: UserCreate, db: Session = Depends(SessionLocal)):
    db_user = db.query(User).filter(User.username == user_data.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    db_user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=get_password_hash(user_data.password),
        role=user_data.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User registered successfully"}