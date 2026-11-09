from __future__ import annotations

import hashlib
import hmac
import os
from datetime import datetime, timedelta, timezone
from typing import Any

from jose import JWTError, jwt

from .config import settings

_ITERATIONS = 120_000


def hash_password(password: str) -> str:
    """PBKDF2-SHA256 哈希，格式: pbkdf2_sha256$iterations$salt_hex$digest_hex。"""
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, _ITERATIONS)
    return f'pbkdf2_sha256${_ITERATIONS}${salt.hex()}${digest.hex()}'


def verify_password(password: str, stored: str) -> bool:
    if not stored:
        return False
    try:
        algo, iterations, salt_hex, digest_hex = stored.split('$')
    except ValueError:
        return False
    if algo != 'pbkdf2_sha256':
        return False
    digest = hashlib.pbkdf2_hmac(
        'sha256', password.encode('utf-8'), bytes.fromhex(salt_hex), int(iterations)
    )
    return hmac.compare_digest(digest.hex(), digest_hex)


def create_access_token(subject: str, extra: dict[str, Any] | None = None) -> str:
    now = datetime.now(timezone.utc)
    payload: dict[str, Any] = {
        'sub': subject,
        'iat': int(now.timestamp()),
        'exp': int((now + timedelta(minutes=settings.token_expire_minutes)).timestamp()),
    }
    if extra:
        payload.update(extra)
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def decode_access_token(token: str) -> dict[str, Any]:
    return jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])


__all__ = [
    'JWTError',
    'create_access_token',
    'decode_access_token',
    'hash_password',
    'verify_password',
]
