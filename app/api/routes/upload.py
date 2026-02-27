from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.security import verify_jwt
from supabase import create_client
from app.core.config import SUPABASE_URL, SUPABASE_ANON_KEY

router = APIRouter()
supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

class UploadMeta(BaseModel):
    title: str
    subject: str

@router.post("/upload")
def upload(meta: UploadMeta, user=Depends(verify_jwt)):

    supabase.table("documents").insert({
        "user_id": user.user.id,
        "title": meta.title,
        "subject": meta.subject
    }).execute()

    return {"status": "stored"}