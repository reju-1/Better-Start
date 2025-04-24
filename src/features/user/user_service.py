from sqlmodel import Session, select
from .user_model import User
from .user_schema import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user_by_email(session: Session, email: str) -> User | None:
    return session.exec(select(User).where(User.email == email)).first()


def create_user(session: Session, user_data: UserCreate) -> User:
    hashed_pw = pwd_context.hash(user_data.password)
    user = User(name=user_data.name, email=user_data.email, hashed_password=hashed_pw)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
