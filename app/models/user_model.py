from sqlalchemy import Column, Integer, String
from app.core.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    nickname = Column(String, unique=True)
    password = Column(String)
