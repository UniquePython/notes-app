"""
Handles all helper functions for auth related services
"""

def get_email_password(data):
    email = data.get("email")
    password = data.get("password")
    return email, password