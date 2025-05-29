from sqlmodel import Session
from src.models.user_models import User


def handle_signup(info: User, session: Session):
    print(f"{'--' *10}\n {info}")
    return {"Message", "User created Successfully"}
