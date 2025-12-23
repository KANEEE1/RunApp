"""API v1 main router - Agrega todos os endpoints."""
from fastapi import APIRouter

from app.api.v1.endpoints import user_endpoints, run_endpoints

api_router = APIRouter()

api_router.include_router(user_endpoints.router, prefix="/users", tags=["users"])
