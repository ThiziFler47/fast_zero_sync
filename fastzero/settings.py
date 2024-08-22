from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        _env_file='.env', _env_file_encoding='utf-8'
    )
    DATABASE_URL: str
