from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import text

from .base import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tg_id: Mapped[int] = mapped_column(unique=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), 
            server_default=text("0"), nullable=False) 