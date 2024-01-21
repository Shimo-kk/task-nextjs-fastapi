import jwt
from datetime import datetime, timedelta

from app.core import JWT_KEY, JWT_ALGORITHM


def encode_jwt(subject: str) -> str:
    payload = {
        "exp": datetime.utcnow() + timedelta(days=1, minutes=0),
        "iat": datetime.utcnow(),
        "sub": subject,
    }
    return jwt.encode(payload, JWT_KEY, algorithm=JWT_ALGORITHM)


def decode_jwt(token: str) -> str:
    try:
        payload = jwt.decode(token, JWT_KEY, algorithms=[JWT_ALGORITHM])
        return payload["sub"]
    except Exception:
        return None
