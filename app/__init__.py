from flask import Flask
from flask_restful import Api
from .config import app_config

def create_app():
    # Initialize flask app
    app_ = Flask(__name__, instance_relative_config=True)

    return app_


app = create_app()
# load from config.py in root folder
app.config.from_object(app_config["development"])
