from configuration.database import db


def initModel():
    db.create_all()
