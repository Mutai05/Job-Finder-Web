# app/__init__.py

from flask import Flask
from .routes.main import main_bp
from .routes.jobs import jobs_bp
from .routes.admin import admin_bp
from .config import Config

def jobfinder_web():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(jobs_bp)
    app.register_blueprint(admin_bp)

    return app
