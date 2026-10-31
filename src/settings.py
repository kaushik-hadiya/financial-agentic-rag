"""Central place for configuration, loaded from environment variables and `.env`."""

from functools import lru_cache
from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """All app settings. Field names map to env vars (case-insensitive)."""

    # hide_input_in_errors: without it, a failed load prints raw values, incl. API keys.
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", hide_input_in_errors=True
    )

    # SecretStr hides the key when settings are printed or logged.
    openrouter_api_key: SecretStr
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    llama_cloud_api_key: SecretStr
    docs_dir: Path = Path("docs")


@lru_cache
def get_settings() -> Settings:
    """Return one shared Settings object, so `.env` is read only once."""
    return Settings()
