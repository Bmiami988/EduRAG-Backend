from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_service import run_rag

router = APIRouter()

class ChatRequest(BaseModel):
    question: str
    mode: str


# ---------------------------
# DEV CHAT (No Auth Required)
# ---------------------------
@router.post("/chat")
def dev_chat(req: ChatRequest):

    answer, difficulty = run_rag(req.question, req.mode)

    return {
        "response": answer,
        "difficulty": difficulty
    }


# ---------------------------
# DEV HEALTH CHECK
# ---------------------------
@router.get("/health")
def health():
    return {"status": "Dev routes working"}