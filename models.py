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
    type_of_test: str
    result: str
    time_of_test: str
    #time_entered: datetime= datetime.now()

class UserResponse(User):
    updated_at: datetime=datetime.now()
    

    
class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional [str]
    date_of_birth: Optional[str]
    roles: Optional[List[Role]]
    type_of_test: Optional [str]
    result: Optional [str]
    time_of_test: Optional [str]
   # time_entered: datetime = datetime.now()
    
    #def __init__(self, **data):
        #super().__init__(**data)
        #self.time_entered = datetime.now() 

    
"""class LabReport:
    type_of_test: str
    result: bool
    time_of_test: datetime.now
    time_entered: str"""
    