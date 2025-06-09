from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class JobDescription(SQLModel, table=True):
    job_id: Optional[int] = Field(default=None, primary_key=True)
    company_id: int = Field(foreign_key="company.company_id")
    title: str
    description: str
    requirements: str
    location: str
    salary_range: str
    posted_at: Optional[str] = Field(default=None)
    is_active: bool = True

    company: Optional["Company"] = Relationship(back_populates="jobs")
    applications: List["JobApplicant"] = Relationship(back_populates="job")


class JobApplicant(SQLModel, table=True):
    application_id: Optional[int] = Field(default=None, primary_key=True)
    job_id: int = Field(foreign_key="jobdescription.job_id")
    user_id: int = Field(foreign_key="user.user_id")
    application_date: Optional[str] = Field(default=None)
    status: str
    resume_url: str
    cover_letter: str

    job: Optional["JobDescription"] = Relationship(back_populates="applications")
    user: Optional["User"] = Relationship(back_populates="applications")
