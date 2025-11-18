import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()


def init_database(app):
    database_url = os.getenv("DATABASE_URL")

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)


def execute_query(query, params=None, fetch_results=True):
    params = params or {}

    with db.engine.connect() as conn:
        result = conn.execute(text(query), params)

        # Se for uma query SELECT, busca os resultados
        if fetch_results and query.strip().upper().startswith("SELECT") or query.strip().upper().startswith("SHOW"):
            return result.fetchall()

        # Para INSERT/UPDATE/DELETE, faz o commit e retorna o número de linhas afetadas
        else:
            conn.commit()
            return result.rowcount
