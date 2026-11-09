from __future__ import annotations

from datetime import datetime, timezone


def utcnow() -> datetime:
    """返回 naive UTC 时间，与数据库中 DATETIME 字段保持一致。"""
    return datetime.now(timezone.utc).replace(tzinfo=None)
