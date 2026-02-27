from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services.rag_service import run_rag
from app.core.security import verify_jwt

router = APIRouter()

class ChatRequest(BaseModel):
    question: str
    mode: str

@router.post("/chat")
def chat(req: ChatRequest, user=Depends(verify_jwt)):

    answer, difficulty = run_rag(req.question, req.mode)

    return {
        "response": answer,
        "difficulty": difficulty
    }