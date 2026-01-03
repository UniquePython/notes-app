"""
Handles authentication-related HTTP routes (login, register, logout).
No business logic should live here.
"""

from flask import Blueprint, request

from app.services.auth import login_user, register_user
from app.utils.auth import get_email_password


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    email, password = get_email_password(data)
    return login_user(email, password), 200


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    email, password = get_email_password(data)
    return register_user(email, password), 201