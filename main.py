from fastapi import FastAPI
import random

app = FastAPI()

#@app.get("/reports")
#def reports():
  #  return{"Data": "Test"}

#@app.get("/labreports")
#def labreports():
   # return{}

lab_Report = {
    1: {
        "First_Name": "Peaches",
        "Last_Name": "Deaches",
        "Date of Birth": "April 17, 2023",
        "Gender":"Female"
    }
}

@app.get("/get-report/{report_id}/{name}")
def get_report(report_id: int, name: str):
    return lab_Report[report_id]