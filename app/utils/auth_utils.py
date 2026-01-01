"""
Handles all helper functions for auth related services
"""

def get_email_password(data):
    email = data.get("email")
    password = data.get("password")
    return email, password


def validate_email_password(email, password):
    if not email:
        raise ValueError("Email is required.")
    if not password:
        raise ValueError("Password is required.")