"""
Business logic related to authentication lives here.
Routes should call these functions instead of implementing logic themselves.
"""

from app.utils.auth import validate_email_password
from app.models import User, db
from app.utils.security import hash_password, verify_password
from app.utils.jwt import create_token


def login_user(email, password):
    validate_email_password(email, password)
    
    user = User.query.filter_by(email=email).first()
    if not user:
        raise ValueError("Invalid email")
    
    if not verify_password(password, user.password_hash):
        raise ValueError("Invalid password")
        
    return {
        "message": "login successful",
        "token": create_token(user.id)
    }


def register_user(email, password):
    validate_email_password(email, password)
    
    existing = User.query.filter_by(email=email).first()
    if existing:
        raise ValueError("User already exists")
    
    user = User(email=email, password_hash=hash_password(password)) # pyright: ignore[reportCallIssue]
    
    db.session.add(user)
    db.session.commit()
    
    return {
        "message": "register successful",
    }