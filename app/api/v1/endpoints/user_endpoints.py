"""User endpoints - Rotas da API para operações de usuários (registro, login, perfil)."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService

router = APIRouter()


@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        return service.create_user(user_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{user_id}", response_model=None, status_code=201)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        service.delete_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.patch("/{user_id}", response_model=UserResponse, status_code=201)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    print("laele")
    service = UserService(db)
    try:
        return service.update_user(user_data, user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
