import os
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    API_URL = '/static/swagger.json'
    SWAGGER_URL = '/api/docs'
    SWAGGER_JSON_URL = '/static/swagger.json'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
