from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.security import verify_jwt
from supabase import create_client
from app.core.config import SUPABASE_URL, SUPABASE_ANON_KEY

router = APIRouter()
supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

class ProgressUpdate(BaseModel):
    topic: str
    score: float

@router.post("/progress")
def update_progress(data: ProgressUpdate, user=Depends(verify_jwt)):

    supabase.table("progress").insert({
        "user_id": user.user.id,
        "topic": data.topic,
        "score": data.score
    }).execute()

    return {"status": "progress updated"}