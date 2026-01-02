import jwt
from datetime import datetime, timedelta, timezone
from flask import current_app


def create_token(user_id: int) -> str:
    payload = {
        "sub": user_id,
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }

    return jwt.encode(
        payload,
        current_app.config["SECRET_KEY"],
        algorithm=current_app.config["JWT_ALGORITHM"]
    )

def decode_token(token: str) -> dict:
    return jwt.decode(
        token,
        current_app.config["SECRET_KEY"],
        algorithms=[current_app.config["JWT_ALGORITHM"]]
    )
