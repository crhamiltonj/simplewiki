import os

from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from config import TestingConfig, DevelopementConfig, ProductionConfig

db = SQLAlchemy()


def create_app(config_class=DevelopementConfig):
    app = Flask(__name__)
    if "PROD" in os.environ and os.environ["PROD"] == "True":
        config_class = ProductionConfig
    app.config.from_object(config_class)

    with app.app_context():
        db.init_app(app)
        register_blueprints(app)

    @app.route("/", methods=["POST", "GET"])
    def root():
        return redirect(url_for("main_index"))

    return app


def register_blueprints(app):
    from api.routes.api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api/v1")

