"""User repository - Gerencia operações de banco de dados para usuários."""

from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate
from app.models import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_data: UserCreate) -> User:
        db_user = User(
            name=user_data.name,
            nickname=user_data.nickname,
            password=user_data.password,
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user

    def get_by_id(self, user_id) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def delete(self, user_id) -> None:
        self.db.query(User).filter(User.id == user_id).delete(synchronize_session=False)
        self.db.commit()

    def update(self, new_data, user_id):
        update_data = new_data.model_dump(exclude_unset=True)
        self.db.query(User).filter(User.id == user_id).update(
            update_data, synchronize_session=False
        )
        self.db.commit()

        # Buscar e retornar o objeto User atualizado
        updated_user = self.db.query(User).filter(User.id == user_id).first()
        return updated_user

    def get_user_by_nickname(self, user_nickname):
        user = self.db.query(User).filter_by(nickname=user_nickname).one_or_none()
        if user:
            return True

        return False
