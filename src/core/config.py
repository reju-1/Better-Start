from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ========= App Info =========
    app_name: str
    version: str = "1.0.0"
    api_prefix: str = "/api/v1"

    # ========= API keys ========
    open_ai: str

    # ========= Database =========
    database_url: str

    # ========= JWT Settings =========
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_expiration_minutes: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
