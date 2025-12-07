"""User repository - Gerencia operações de banco de dados para usuários."""
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.models import User

class UserRepository():
    def __init__(self, db:Session):
        self.db = db

    def create(self, user_data: UserCreate) -> User:
        db_user = User(
            name = user_data.name,
            nickname = user_data.nickname,
            password = user_data.password
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user
    
    def get_user_by_nickname(self, user_nickname):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        user = self.db.query(User).filter_by(nickname=user_nickname).one_or_none()
        if user:
            return True
        
        return False