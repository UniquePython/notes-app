"""
Handles authentication-related HTTP routes (login, register, logout).
No business logic should live here.
"""

from flask import Blueprint


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["POST"])
def login():
    return {"message": "login endpoint placeholder"}


@auth_bp.route("/register", methods=["POST"])
def register():
    return {"message": "register endpoint placeholder"}