from pydantic import BaseModel
from pydantic_settings import BaseSettings

class RunConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000


class ApiPrefix (BaseModel):
    choice_prefix: str = "/choice"

class Settings(BaseSettings):
    run: RunConfig = RunConfig
    api: ApiPrefix = ApiPrefix()

settings: Settings = Settings