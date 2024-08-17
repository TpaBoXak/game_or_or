from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import text

from .base import Base

class UserJoke(Base):
    __tablename__ = "users_jokes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False) 
    joke_id: Mapped[int] = mapped_column(ForeignKey("jokes.id"), nullable=False) 