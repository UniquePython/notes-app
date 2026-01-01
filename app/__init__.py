"""
Creates a Flask app, registers routes and initializes database.
"""

from flask import Flask


def create_app():
    app = Flask(__name__.split(".")[0])
    
    from app.routes.health import health_bp
    from app.routes.auth import auth_bp
    
    bps = [health_bp, auth_bp]
    
    for bp in bps:
        app.register_blueprint(bp)
    
    return app