from flask import Blueprint, render_template


api_bp = Blueprint("api_bp", __name__)


@api_bp.route("/")
def root():
    return "Hello World"
