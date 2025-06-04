from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlmodel import Session

# Internal imports
from src.core.db import get_session
from . import user_schemas as schema
from . import user_controller as controller


DBSession = Annotated[Session, Depends(get_session)]
router = APIRouter(prefix="/users")


@router.get("/login", response_model=schema.LoginResponse)
def login_handler(user_data: schema.LoginData, session: DBSession):
    return controller.handle_login(user_data, session)


@router.post(
    "/signup",
    response_model=schema.SignupResponse,
    status_code=status.HTTP_201_CREATED,
)
def signup_handler(user_data: schema.SignupData, session: DBSession):
    return controller.handle_signup(user_data, session)
