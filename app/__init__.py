from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.models import DataBaseHelper
from config import settings
from app.api import router
from .models import Base

db_helper = DataBaseHelper(
        url=str(settings.db.url),
        echo=settings.db.echo,
        echo_pool=settings.db.echo_pool,
        pool_size=settings.db.pool_size,
        max_overflow=settings.db.max_overflow,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    print("dispose engine")
    await db_helper.dispose()

main_app = FastAPI(lifespan=lifespan)
main_app.include_router(router=router, prefix=settings.api.choice_prefix)

