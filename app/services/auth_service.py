"""
Business logic related to authentication lives here.
Routes should call these functions instead of implementing logic themselves.
"""

from app.utils.auth_utils import validate_email_password


def login_user(email, password):
    # Placeholder logic
    validate_email_password(email, password)
    
    return {
        "message": "login service called",
        "email": email
    }


def register_user(email, password):
    # Placeholder logic
    validate_email_password(email, password)
    
    return {
        "message": "register service called",
        "email": email
    }