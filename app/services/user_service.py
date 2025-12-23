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

    def delete_user(self, user_id):
        return self.repository.delete(user_id)

    def update_user(self, new_user_data, user_id):
        user = self.repository.get_by_id(user_id)
        if not user:
            raise ValueError("Usuário não encontrado")

        return self.repository.update(new_user_data, user_id)
