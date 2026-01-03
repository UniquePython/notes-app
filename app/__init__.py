"""
Creates a Flask app, registers routes and initializes database.
"""

from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_cors import CORS
from app.models import db
from .config import Config


def create_app():
    app = Flask(__name__.split(".")[0])
    CORS(app)
    app.config.from_object(Config)

    
    db.init_app(app)
    
    from app.routes.health import health_bp
    from app.routes.auth import auth_bp
    from app.routes.notes import notes_bp
    
    bps = [health_bp, auth_bp, notes_bp]
    
    for bp in bps:
        app.register_blueprint(bp)
    
    @app.errorhandler(ValueError)
    def handle_value_error(e):
        return {"error": str(e)}, 400

    @app.errorhandler(Exception)
    def handle_generic_error(e):
        return {"error": "Internal server error"}, 500
        # return {"error": str(e)}, 500
    
    return app