from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()

__all_ = [
    "db",
]
