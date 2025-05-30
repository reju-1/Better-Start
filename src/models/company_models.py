from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class Company(SQLModel, table=True):
    company_id: Optional[int] = Field(default=None, primary_key=True)
    company_name: str = Field(unique=True)
    address: str
    city: str
    country: str
    website: str
    created_at: Optional[str] = Field(default=None)

    members: List["CompanyMember"] = Relationship(back_populates="company")
    jobs: List["JobDescription"] = Relationship(back_populates="company")


class CompanyMember(SQLModel, table=True):
    member_id: Optional[int] = Field(default=None, primary_key=True)
    company_id: int = Field(foreign_key="company.company_id")
    user_id: int = Field(foreign_key="user.user_id")
    role: str
    joined_at: Optional[str] = Field(default=None)

    company: Optional["Company"] = Relationship(back_populates="members")
    user: Optional["User"] = Relationship(back_populates="memberships")
