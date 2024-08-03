from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

from models import Base

class User(Base):
    __tablename__ = "users"
