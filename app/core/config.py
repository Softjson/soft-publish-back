from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    env: str = "development"
    database_url: str 
    gemini_api_key: str 
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()