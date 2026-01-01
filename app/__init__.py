"""
Creates a Flask app, registers routes and initializes database.
"""

from flask import Flask


def create_app():
    app = Flask(__name__.split(".")[0])
    
    from app.routes.health import health_bp
    
    app.register_blueprint(health_bp)
    
    return app