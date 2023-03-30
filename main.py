from fastapi import FastAPI, Path
from uuid import uuid4
from typing import List
from models import User, Role, Gender

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        first_name= "Peaches",
        last_name="Baldeaches",
        date_of_birth="October 17, 1934",
        gender=Gender.female,
        roles=[Role.user]
        ),
    User(
        id=uuid4(), 
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
#here is where I return the entire database

#@app.get("/reports")
#def reports():
  #  return{"Data": "Test"}

#@app.get("/labreports")
#def labreports():
   # return{}

"""patient = {
    1: {
        "name": "Peaches",
        "lastName": "Deaches",
        "Date of Birth": "April 17, 2023",
        "Gender":"Female"
    }
},"""


"""@app.get("/get-patient/{patient_id}")
def get_patient(patient_id: int = Path(description="The ID of the patient you would like to view")):
    return patient[patient_id]"""

"""@app.get("/get-by-name")
def get_patient(name: str):
    for patient_id in patient:
        if patient[patient_id]["name"] == name:
            return patient[patient_id]
        return{"Data": "Not Found"}"""