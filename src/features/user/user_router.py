from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlmodel import Session

# Internal imports
from src.core.db import get_session
from src.models import user_models
from . import user_response_schema
from . import user_controller


DBSession = Annotated[Session, Depends(get_session)]
router = APIRouter(prefix="/users")


@router.post(
    "/signup",
    response_model=user_response_schema.UserCreate,
    status_code=status.HTTP_201_CREATED,
)
def signup(user_data: user_models.User, session: DBSession):
    return user_controller.handle_signup(user_data, session)
