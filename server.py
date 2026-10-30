from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NumberPayload(BaseModel):
    num1: float
    num2: float

@app.post("/add")
async def add_numbers(payload: NumberPayload):
    result = payload.num1 + payload.num2
    return {"sum": result}