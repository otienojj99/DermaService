from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import decode_jwt


security = HTTPBearer()

class CurrentUser:
    def __init__(self, user_id: str, role: str):
        self.id = user_id
        self.role = role
        
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security),)->CurrentUser:
    payload = decode_jwt(credentials.credentials)
    
    user_id = payload.get("sub")
    role = payload.get("role")
    
    if not user_id or not role:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
        )
        
    return CurrentUser(user_id=user_id, role=role)

def require_dermatologist(user: CurrentUser = Depends(get_current_user)):
    if user.role != "dermatologist":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Dermatologist access required",
        )
    return user

def require_admin(user: CurrentUser = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )
    return user