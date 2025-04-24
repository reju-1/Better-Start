from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from .user_schema import UserCreate, UserLogin, UserRead
from .user_service import create_user
from .user_auth import authenticate_user, create_access_token, get_current_user
from core.db import get_session

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/signup", response_model=UserRead)
def signup(user_data: UserCreate, session: Session = Depends(get_session)):
    if authenticate_user(
        session, UserLogin(email=user_data.email, password=user_data.password)
    ):
        raise HTTPException(status_code=400, detail="User already exists")
    user = create_user(session, user_data)
    return user


@router.post("/login")
def login(user_data: UserLogin, session: Session = Depends(get_session)):
    user = authenticate_user(session, user_data)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", response_model=UserRead)
def read_me(current_user=Depends(get_current_user)):
    return current_user
