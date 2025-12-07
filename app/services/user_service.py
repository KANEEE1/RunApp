"""User service - Lógica de negócio relacionada a usuários."""
from sqlalchemy.orm import Session

from app.schemas import UserCreate
from app.repositories import UserRepository


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        

    def create_user(self, user_data: UserCreate):
        if self.repository.get_user_by_nickname(user_data.nickname):
            raise ValueError("Esse nickname já existe.")
        return self.repository.create(user_data)
