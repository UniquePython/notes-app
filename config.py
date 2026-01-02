import os
import secrets


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex(256))
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///notes.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False