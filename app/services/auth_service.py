"""
Business logic related to authentication lives here.
Routes should call these functions instead of implementing logic themselves.
"""

from app.utils.auth_utils import validate_email_password
from app.models import User, db
from app.utils.security import hash_password


def login_user(email, password):
    # Placeholder logic
    validate_email_password(email, password)
    
    return {
        "message": "login service called",
        "email": email
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
        "message": "register service called",
        "email": email
    }