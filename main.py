from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List, Optional
from datetime import datetime
from models import User, Role, Gender, UserUpdateRequest, UserResponse

app = FastAPI()


db: List[User] = [
    User(
        id=UUID("d18d6cf9-3d79-43cb-87a9-17b5d247d764"), 
        first_name= "Peaches",
        last_name="Baldeaches",
        date_of_birth="October 17, 1934",
        gender=Gender.female,
        roles=[Role.user],
        type_of_test= "Glucose",
        result= "Postive",
        time_of_test= "3PM"
   
    ),
    User(
        id=UUID("2f6a369a-ec64-4319-9f5b-ab0e0ab0b0f3"), 
        first_name= "George",
        last_name="Pineapple",
        date_of_birth="March 17, 2023",
        gender=Gender.male,
        roles=[Role.admin, Role.user],
        type_of_test="Blood Test",
        result= "Negative",
        time_of_test= "4PM"
    ),
    User(
        id=UUID("3a84f00b-71f9-4d2a-8c04-53aef917bb48"), 
        first_name= "Jane",
        last_name="Doe",
        date_of_birth="January 1, 1980",
        gender=Gender.female,
        roles=[Role.user],
        type_of_test="Lab Report",
        result= "Pending",
        time_of_test= ""
    ),
]


##The opening page
@app.get("/")
async def root():
    return {"Welcome to the": "Patient Portal"}

##This shows all patients
@app.get("/api/v1/users")
async def fetch_users():
    return db;

##This shows all patients by the test type
@app.get("/api/v1/users/test{test_type}")
async def get_user_by_test(test_type: str):
    users_info = []
    for user in db:
        if user.type_of_test == test_type:
            user_info = {
                "id": user.id,
                 "first_name": user.first_name,
                "last_name": user.last_name,
                "date_of_birth": user.date_of_birth,
                "gender": user.gender,
                "roles": user.roles,
                "type_of_test": user.type_of_test,
                "result": user.result,
                "time_of_test": user.time_of_test
            }
            users_info.append(user_info)
    if not users_info:
        raise HTTPException(status_code=404, detail=f"No users found with test type: {test_type}")
    return users_info
            
##This is how you would register a patient
@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

##Here you can delete the patient
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )
"""@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            
            if user_update.first_name !=None:
                user[user_id].first_name = user_update.first_name
            if user_update.last_name != None:
                user[user_id].last_name = user_update.last_name
            if user_update.date_of_birth != None:
                user[user_id].date_of_birth = user_update.date_of_birth
            if user_update.roles != None:
                user[user_id].roles = user_update.roles
            return
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exist"
        )"""

##Here is where you can update a patient's information
@app.put("/api/v1/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: UUID, user_update: UserUpdateRequest):
    try:
        user = next(user for user in db if user.id == user_id)
    except StopIteration:
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exist"
        )

    if user_update.first_name:
        user.first_name = user_update.first_name
    if user_update.last_name:
        user.last_name = user_update.last_name
    if user_update.date_of_birth:
        user.date_of_birth = user_update.date_of_birth
    if user_update.roles:
        user.roles = user_update.roles
    if user_update.type_of_test:
        user.type_of_test = user_update.type_of_test
    if user_update.result:
        user.result = user_update.result
    if user_update.time_of_test:
        user.time_of_test = user_update.time_of_test
    
    

    return UserResponse(**user.dict())

"""@app.get("/api/v1/users/test/{test_type}")
async def get_user_by_test(test_type: str, start_date: str, end_date: str):
    users_info = []
    for user in db:
        if user.type_of_test == test_type:
            user_time_of_test = datetime.strptime(user.time_of_test, '%I%p')
            start = datetime.strptime(start_date, '%Y-%m-%d %I%p')
            end = datetime.strptime(end_date, '%Y-%m-%d %I%p')
            if start <= user_time_of_test <= end:
                user_info = {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "date_of_birth": user.date_of_birth,
                    "gender": user.gender,
                    "roles": user.roles,
                    "type_of_test": user.type_of_test,
                    "result": user.result,
                    "time_of_test": user.time_of_test
                }
                users_info.append(user_info)
    if not users_info:
        raise HTTPException(status_code=404, detail=f"No users found with test type: {test_type}")
    return users_info"""
        
# show all patients that have had a certain type of lab report in a datetime range.
     



