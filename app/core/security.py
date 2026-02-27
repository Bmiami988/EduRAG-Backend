from fastapi import Request, HTTPException
from jose import jwt, JWTError
from app.core.config import SUPABASE_JWT_SECRET

ALGORITHM = "HS256"

def verify_jwt(request: Request):
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        raise HTTPException(status_code=401, detail="Missing token")

    try:
        token = auth_header.split(" ")[1]
        payload = jwt.decode(token, SUPABASE_JWT_SECRET, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")