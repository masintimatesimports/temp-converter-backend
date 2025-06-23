from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TempInput(BaseModel):
    celsius: float

@app.post("/convert")
def convert_temperature(data: TempInput):
    fahrenheit = (data.celsius * 9/5) + 32
    return {"fahrenheit": fahrenheit}