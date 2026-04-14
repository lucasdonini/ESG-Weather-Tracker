from pydantic_settings import BaseSettings


class EnvVariables(BaseSettings):
    db_url: str
    db_name: str
    latitude: float
    longitude: float

    model_config = {"env_file": ".env"}


env: EnvVariables = EnvVariables()
