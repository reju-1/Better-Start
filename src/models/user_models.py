from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date


# SQLModel User class
class User(SQLModel, table=True):

    # Primary key
    id: Optional[int] = Field(default=None, primary_key=True)

    # Required fields
    name: str = Field(max_length=255)
    email: str = Field(max_length=255, unique=True)
    password: str = Field(max_length=255)

    # Optional fields
    phone_no: Optional[str] = None
    dob: Optional[date] = None
    bio: Optional[str] = None

    # Social media links (optional)
    linkedin: Optional[str] = Field(default=None, max_length=255)
    twitter: Optional[str] = Field(default=None, max_length=255)  # Twitter/X
    github: Optional[str] = Field(default=None, max_length=255)
    photo: Optional[str] = Field(default=None, max_length=255)
