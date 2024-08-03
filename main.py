from fastapi import FastAPI
import uvicorn

from app.api import router
from config import settings

app = FastAPI()
app.include_router(router=router, prefix=settings.api.choice_prefix)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)