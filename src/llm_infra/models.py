from pydantic import BaseModel

class ChatRequest(BaseModel):
    query : str
    model : str | None = "default"
