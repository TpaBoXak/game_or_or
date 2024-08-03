from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base

class User(Base):
    __tablename__ = "users"
    tg_id: Mapped[int] = mapped_column(unique=True)
