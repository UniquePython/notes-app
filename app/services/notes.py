from app.models import Note, db


def create_note(user, title, content):
    if not title:
        raise ValueError("Title is required")
    if not content:
        raise ValueError("Content is required")

    note = Note(
        title=title, # pyright: ignore[reportCallIssue]
        content=content, # pyright: ignore[reportCallIssue]
        user_id=user.id # pyright: ignore[reportCallIssue]
    )

    db.session.add(note)
    db.session.commit()

    return {
        "id": note.id,
        "title": note.title,
        "content": note.content
    }


def list_notes(user):
    notes = Note.query.filter_by(user_id=user.id).all()

    return [
        {"id": n.id, "title": n.title, "content": n.content}
        for n in notes
    ]


def list_note(user, note_id):
    note = Note.query.filter_by(id=note_id, user_id=user.id).first()
    if not note:
        raise ValueError("Note not found")
    
    return {
        "id": note.id,
        "title": note.title,
        "content": note.content
    }


def update_note(user, note_id, title, content):
    note = Note.query.filter_by(id=note_id, user_id=user.id).first()
    if not note:
        raise ValueError("Note not found")

    if title:
        note.title = title
    if content:
        note.content = content

    db.session.commit()

    return {
        "id": note.id,
        "title": note.title,
        "content": note.content
    }


def delete_note(user, note_id):
    note = Note.query.filter_by(id=note_id, user_id=user.id).first()
    if not note:
        raise ValueError("Note not found")

    db.session.delete(note)
    db.session.commit()

    return {"message": "Note deleted"}
