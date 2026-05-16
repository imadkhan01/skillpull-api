from fastapi import APIRouter

from app.api.routes import auth, profile, company, jobs, ai
from app.api.routes.health import router as health

api_router = APIRouter()

api_router.include_router(health, prefix="/health", tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(profile.router, prefix="/profile", tags=["profile"])
api_router.include_router(company.router, prefix="/company", tags=["company"])
api_router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])
