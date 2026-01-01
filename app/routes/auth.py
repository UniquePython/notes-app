"""
Handles authentication-related HTTP routes (login, register, logout).
No business logic should live here.
"""

from flask import Blueprint, request

from app.services.auth_service import login_user, register_user
from app.utils.auth_utils import get_email_password


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    email, password = get_email_password(data)
    result = login_user(email, password)
    return result


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    email, password = get_email_password(data)
    result = register_user(email, password)
    return result