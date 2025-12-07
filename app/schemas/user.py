"""User schemas - Define como os dados de usuário entram e saem da API."""
from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    nickname: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    nickname: Optional[str] = None
    password: Optional[str] = None

class UserResponse(UserBase):
    id: int
    
    class Config:
        from_attributes = True
