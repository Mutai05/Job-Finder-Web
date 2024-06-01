# app/__init__.py

from flask import Flask
from .routes.main import main_bp
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints

    app.register_blueprint(main_bp)

    return app