"""
Handles all helper functions for auth related services
"""

from functools import wraps
from flask import request
from app.utils.jwt import decode_token
from app.models import User


def get_email_password(data):
    email = data.get("email")
    password = data.get("password")
    return email, password


def validate_email_password(email, password):
    if not email:
        raise ValueError("Email is required.")
    if not password:
        raise ValueError("Password is required.")


def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            raise ValueError("Authentication required")

        token = auth_header.split(" ")[1]
        payload = decode_token(token)

        user = User.query.get(payload["sub"])
        if not user:
            raise ValueError("Invalid token")

        return fn(user, *args, **kwargs)

    return wrapper