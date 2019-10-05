from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from config import DevelopmentConfig, ProductionConfig

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    with app.app_context():
        db.init_app(app)
        register_blueprints(app)

    return app


def register_blueprints(app):
    from api.routes.api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api/v1")

