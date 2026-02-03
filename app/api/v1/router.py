from fastapi import APIRouter
from app.api.v1 import dermatologist

api_router = APIRouter()

api_router.include_router(
    dermatologist.router,
    prefix="/dermatologists",
    tags=["Dermatologists"]
)
