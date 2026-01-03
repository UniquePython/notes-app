# Notes App (Full Stack)

A full-stack notes application with user authentication, JWT-based authorization, and user-owned CRUD functionality, built with Flask and a minimal vanilla JavaScript frontend.


## Features

- User registration and login

- Secure password hashing (bcrypt)

- JWT-based authentication

- Protected API routes

- User-owned notes (no cross-user access)

- Create, read, update, and delete notes

- Minimal frontend to demonstrate full-stack flow


## Tech Stack

### Backend

- Python

- Flask

- Flask-SQLAlchemy

- SQLite (development)

- JWT (PyJWT)

- bcrypt

- pytest

### Frontend

- HTML

- Vanilla JavaScript (Fetch API)

- LocalStorage for JWT persistence


## Project Structure

```
.
├── app
│   ├── __init__.py        # App factory & global error handling
│   ├── models.py          # Database models
│   ├── routes             # HTTP routes (thin controllers)
│   │   ├── auth.py
│   │   └── notes.py
│   ├── services           # Business logic
│   │   ├── auth_service.py
│   │   └── notes_service.py
│   └── utils              # Reusable utilities
│       ├── auth.py        # Auth decorator
│       ├── jwt.py         # JWT creation & verification
│       └── security.py    # Password hashing
│   ├── config.py          # Configuration
├── frontend
│   ├── index.html
│   └── app.js
├── tests                  # Automated tests
├── run.py                 # Application entry point
└── README.md
```

## Setup and Running the Project

1. Clone the repository
```
git clone https://github.com/UniquePython/notes-app.git
cd notes-app
```

2. Create a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```
pip3 install -r requirements.txt
```

4. Run the backend
```
python3 run.py
```

The API will be available at: http://127.0.0.1:5000

5. Run the frontend

Open `frontend/index.html` in your browser.