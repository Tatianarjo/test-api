from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum
from datetime import datetime

class Gender(str, Enum):
    male = "male"
    female = "female"
    
class Role(str, Enum):
    admin = "admin"
    user = "user"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    date_of_birth: str
    gender: Gender
    roles: List[Role]

class UserResponse(User):
    updated_at: datetime=datetime.now()
    

    
class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional [str]
    date_of_birth: Optional[str]
    roles: Optional[List[Role]]
    
"""class UserUpdateRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional [str] = None
    date_of_birth: Optional[str] = None
    roles: Optional[List[Role]] = None"""
    