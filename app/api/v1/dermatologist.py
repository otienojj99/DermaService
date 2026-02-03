from fastapi import APIRouter, Depends
from app.api.deps import require_dermatologist

router = APIRouter()

@router.get("/me")
async def get_my_profile(user=Depends(require_dermatologist)):
    return {
        "message": "Authenticated dermatologist",
        "user_id": user.id,
    }
