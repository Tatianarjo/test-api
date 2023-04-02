from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Role, Gender, UserUpdateRequest, UserResponse

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("d18d6cf9-3d79-43cb-87a9-17b5d247d764"), 
        first_name= "Peaches",
        last_name="Baldeaches",
        date_of_birth="October 17, 1934",
        gender=Gender.female,
        roles=[Role.user]
        ),
    User(
        id=UUID("2f6a369a-ec64-4319-9f5b-ab0e0ab0b0f3"), 
        first_name= "George",
        last_name="Pineapple",
        date_of_birth="March 17, 2023",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
        )
]

@app.get("/")
async def root():
    return {"Welcome to the": "Patient Portal"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

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

    return UserResponse(**user.dict())

        

     

#here is where I return the entire database with the addition of a new user and their id




