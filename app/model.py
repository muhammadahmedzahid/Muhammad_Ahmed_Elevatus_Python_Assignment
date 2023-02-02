from pydantic import BaseModel
from typing import Literal, Optional
from dataclasses import dataclass


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Muhammad",
                "last_name": "Ahmed",
                "email": "ahmedzahid212121@gmail.com"
            }
        }


class CandidateCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    career_level: str
    job_major: str
    years_of_experience: int
    degree_type: str
    skills: list
    nationality: str
    city: str
    salary: float
    gender: Literal["Male", "Female", "Not Specific"]

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Muhammad",
                "last_name": "Ahmed",
                "email": "ahmedzahid2121@gmail.com",
                "career_level": "senior",
                "job_major": "Engineering",
                "years_of_experience": "8",
                "degree_type": "Bachelor",
                "skills": ["Python", "WebApps"],
                "nationality": "pakistani",
                "city": "Daska",
                "salary": "5000",
                "gender": "Male"
            }
        }


class CandidateUpdate(BaseModel):
    first_name: str = None
    last_name: str = None
    career_level: str = None
    job_major: str = None
    years_of_experience: int = None
    degree_type: str = None
    skills: list = None
    nationality: str = None
    city: str = None
    salary: float = None
    gender: Literal["Male", "Female", "Not Specific"] = None

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Muhammad",
                "last_name": "Ahmed",
                "career_level": "senior",
                "job_major": "Engineering",
                "years_of_experience": "8",
                "degree_type": "Bachelor",
                "skills": ["Python", "WebApps"],
                "nationality": "pakistani",
                "city": "Daska",
                "salary": "5000",
                "gender": "Male"
            }
        }


@dataclass
class CandidateSearch:
    candidate_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    career_level: Optional[str] = None
    job_major: Optional[str] = None
    years_of_experience: Optional[int] = None
    degree_type: Optional[str] = None
    skills: Optional[list] = None
    nationality: Optional[str] = None
    city: Optional[str] = None
    salary: Optional[float] = None
    gender: Optional[Literal["Male", "Female", "Not Specific"]] = None

    class Config:
        schema_extra = {
            "example": {
                "candidate_id": "63dbe42c3dc8c0e29daced06",
                "first_name": "Muhammad",
                "last_name": "Ahmed",
                "email": "ahmedzahid2121@gmail.com",
                "career_level": "senior",
                "job_major": "Engineering",
                "years_of_experience": "8",
                "degree_type": "Bachelor",
                "skills": ["Python", "WebApps"],
                "nationality": "pakistani",
                "city": "Daska",
                "salary": "5000",
                "gender": "Male"
            }
        }


@dataclass
class UserLogin:
    first_name: str
    last_name: str
    email: str

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Muhammad",
                "last_name": "Ahmed",
                "email": "ahmedzahid212121@gmail.com"
            }
        }
