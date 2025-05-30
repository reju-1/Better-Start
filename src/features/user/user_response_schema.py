from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    # email: EmailStr # ab.com
    password: str


class UserRead(BaseModel):
    id: int
    name: str
    # email: EmailStr


class UserLogin(BaseModel):
    # email: EmailStr
    password: str
