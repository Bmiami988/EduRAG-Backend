from fastapi import Depends
from app.core.security import verify_jwt

def get_current_user(payload: dict = Depends(verify_jwt)):
    return payload