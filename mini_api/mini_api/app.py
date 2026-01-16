from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Mini API", version="1.0.0")

class PingResponse(BaseModel):
    status: str
    time: str

class SumRequest(BaseModel):
    a: float
    b: float

class SumResponse(BaseModel):
    result: float

@app.get("/ping", response_model=PingResponse)
def ping():
    return {"status": "ok", "time": datetime.now().isoformat(timespec="seconds")}

@app.post("/sum", response_model=SumResponse)
def calc_sum(date: SumResponse):
    return {"result": date.a + date.b}
