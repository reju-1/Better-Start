from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from authlib.jose import jwt
from authlib.jose.errors import JoseError
from passlib.context import CryptContext

from src.core.config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# --- JWT TOKEN UTILS ---


def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=settings.jwt_expiration_minutes)
    )

    to_encode.update({"exp": expire})
    token = jwt.encode(
        header={"alg": settings.jwt_algorithm},
        payload=to_encode,
        key=settings.jwt_secret_key,
    )
    return token.decode("utf-8")


def decode_access_token(token: str):
    try:
        return jwt.decode(token, settings.JWT_SECRET_KEY)
    except JoseError:
        return None


# --- JWT DEPENDENCY ---


def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception

    username: str = payload.get("sub")
    if username is None:
        raise credentials_exception

    return username  # or you could return full user object from DB


# --- PASSWORD UTILS ---


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
