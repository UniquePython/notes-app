"""
Responds with status ok if app is running.
"""

from flask import Blueprint


health_bp = Blueprint("health", __name__)


@health_bp.route("/health")
def health():
    return {"status": "ok"}