"""API v1 main router - Agrega todos os endpoints."""
from fastapi import APIRouter

from app.api.v1.endpoints import users, runs

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
