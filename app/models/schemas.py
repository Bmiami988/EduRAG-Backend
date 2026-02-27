from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str
    mode: str

class ChatResponse(BaseModel):
    response: str
    difficulty: str