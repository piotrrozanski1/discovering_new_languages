import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = SQLAlchemy()
Base = db.Model
session = db.session

# engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], pool_size=10)  # Set pool size to 10
#
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()
# db = SessionLocal()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     except:
#         db.close()
