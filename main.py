from fastapi import FastAPI, Path
from uuid import UUID
from typing import List
from models import User, Role, Gender

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

#here is where I return the entire database with the addition of a new user and their id




