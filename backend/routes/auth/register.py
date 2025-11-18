from flask import Blueprint
register_bp = Blueprint("register", __name__, url_prefix="/register")


@register_bp.get("/")
def index():
    return {
        "register": "ok",
    }
