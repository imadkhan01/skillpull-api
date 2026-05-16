from fastapi import APIRouter

from app.api.routes.health import router as health

router = APIRouter()

router.include_router(health, prefix="/health", tags=["health"])
