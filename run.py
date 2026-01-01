"""
Entry point of the application.
Responsible only for starting the app.
"""

from app import create_app


app = create_app()

if __name__ == "__main__":
    app.run()