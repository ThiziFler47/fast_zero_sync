from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        _env_file='.env', _env_file_encoding='utf-8'
    )
    DATABASE_URL: str
