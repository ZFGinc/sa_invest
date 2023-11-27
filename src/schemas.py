from typing import List, Optional
from pydantic import BaseModel
from .enums import *


class UserBase(BaseModel):
    id: int
    firstName: str
    lastName: str
    middleName: str
    email: str
    role_code: role_code_type


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
        
class ProjectBase(BaseModel):
    id: int
    user_id: int
    owner_id: int
    address_id: int
    industry_id: int
    name: str
    application_own_amount: float
    application_support_amount: float
    work_place_count: int
    nalog_amount: int
    description: str
    state: project_state_type
    
class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True