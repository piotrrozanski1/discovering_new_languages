from app import app, db
from application.model import product


def update_db_schema():
    app.app_context().push()
    db.create_all()
    db.session.commit()
