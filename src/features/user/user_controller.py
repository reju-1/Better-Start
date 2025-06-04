from sqlmodel import Session
from src.models.user_models import User
from datetime import datetime

from user_schemas import LoginData, LoginResponse
from user_schemas import SignupData, SignupResponse


def handle_signup(info: SignupData, session: Session) -> SignupResponse:
    print(f"{'--' *10}\n {info}")
    return {"name": "Rej", "password": f"{datetime.now()}"}


def handle_login(info: LoginData, session: Session) -> LoginResponse:
    print(f"{'--' *10}\n {info}")
    return {"name": "Rej", "password": f"{datetime.now()}"}
