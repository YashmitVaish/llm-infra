import logging

from fastapi import FastAPI

from .middlewares.logger import LoggingMiddleware
from .models import ChatRequest

logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.add_middleware(LoggingMiddleware)


@app.post("/chat")
async def chat(req: ChatRequest):
    return f"hey you asked about {req.query} from {req.model}"
