from flask import Blueprint
recover_bp = Blueprint("recover", __name__, url_prefix="/recover")


@recover_bp.get("/")
def index():
    return {
        "recover": "ok",
    }
