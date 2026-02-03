from pathlib import Path
from jose import jwt
from fastapi import HTTPException, status
from app.core.config import settings


def load_public_key()->str:
    try:
        return Path(settings.JWT_PUBLIC_KEY_PATH).read_text()
    except Exception:
        raise RuntimeError("JWT public key not found")
    
    
def decode_jwt(token: str)->dict:
    try:
        payload = jwt.decode(
            token,
            load_public_key(),
            algorithms=[settings.JWT_ALGORITHM],
            options={"verify_aud": False},
        )
        return payload
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
    