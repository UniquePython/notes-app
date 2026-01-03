from flask import Blueprint, request
from app.services.notes import (
    create_note,
    list_note,
    list_notes,
    update_note,
    delete_note
)
from app.utils.auth import login_required



notes_bp = Blueprint("notes", __name__, url_prefix="/notes")

@notes_bp.route("", methods=["POST"])
@login_required
def create(user):
    data = request.get_json() or {}
    return create_note(
        user,
        data.get("title"),
        data.get("content")
    ), 201


@notes_bp.route("", methods=["GET"])
@login_required
def list_all(user):
    return list_notes(user), 200


@notes_bp.route("/<int:note_id>", methods=["GET"])
@login_required
def list_specific(user, note_id):
    return list_note(user, note_id), 200


@notes_bp.route("/<int:note_id>", methods=["PUT"])
@login_required
def update(user, note_id):
    data = request.get_json() or {}
    return update_note(
        user,
        note_id,
        data.get("title"),
        data.get("content")
    ), 200


@notes_bp.route("/<int:note_id>", methods=["DELETE"])
@login_required
def delete(user, note_id):
    return delete_note(user, note_id), 200
