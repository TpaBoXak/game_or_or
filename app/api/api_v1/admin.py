from fastapi import APIRouter
from config import settings

router: APIRouter = APIRouter(prefix=settings.api.admin_prefix)