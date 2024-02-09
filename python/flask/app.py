from config import Config
from configuration.database import db
from flask import Flask, render_template
from application.api.api import ApiConfig
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
ApiConfig(app)

swaggerui_blueprint = get_swaggerui_blueprint(app.config["SWAGGER_URL"], app.config["API_URL"],
                                              config={'app_name': "Fruit shop"})

app.register_blueprint(swaggerui_blueprint)
