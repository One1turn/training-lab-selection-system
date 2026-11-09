from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(PROJECT_ROOT / '.env'),
        env_file_encoding='utf-8',
        extra='ignore',
    )

    app_name: str = '实训室选组选拔系统'
    app_version: str = '0.2.0'
    database_url: str = 'sqlite:///./data/app.db'
    secret_key: str = 'change-me-in-production'
    algorithm: str = 'HS256'
    token_expire_minutes: int = 720
    demo_mode: bool = True
    enforce_time_window: bool = False
    waitlist_min_size: int = 3
    internal_candidate_ratio: float = 0.2
    cors_origins: str = '*'

    @property
    def cors_origin_list(self) -> list[str]:
        raw = (self.cors_origins or '').strip()
        if raw in ('', '*'):
            return ['*']
        return [x.strip() for x in raw.split(',') if x.strip()]


settings = Settings()
