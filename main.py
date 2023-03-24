from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/reports")
def reports():
    return{"Data": "Test"}