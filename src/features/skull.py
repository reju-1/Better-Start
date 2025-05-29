from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlmodel import Session

# Internal imports
from src.core.db import get_session
from src.models import user_models
from . import schema_file
from . import controller_file

DBSession = Annotated[Session, Depends(get_session)]
router = APIRouter(prefix="/abc")


@router.post("/name", response_model=schema_file.responseSchema)
def function_name(user_data: schema_file.responseSchema, session: DBSession):
    return controller_file.function_name(user_data, session)
