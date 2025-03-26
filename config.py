from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PG_HOST: str
    PG_PORT: str
    PG_USER: str
    PG_PASSWORD: str
    PG_NAME: str

    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.PG_USER}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_NAME}"

    @property
    def DATABASE_URL_psycopg(self):
        return f"postgresql+psycopg://{self.PG_USER}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_NAME}"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()