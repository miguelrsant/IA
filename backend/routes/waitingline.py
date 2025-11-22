from flask import Blueprint
waitingline_bp = Blueprint("waitingline", __name__, url_prefix="/waitingline")


@waitingline_bp.post("/")
def index():
    return {
        "singin": "ok",
    }
