from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class chatRequest(BaseModel):
    query : str
    model : str | None


@app.post("/chat")
async def chat(req : chatRequest):
    return f"hey {req.query} || {req.model}"
