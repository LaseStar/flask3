from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from blog.article.views import article
from blog.auth.views import auth_app
from blog.user.views import users_app

from blog.models.database import db
from blog.views.auth import login_manager


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "abcdefg123456"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////blog.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    login_manager.init_app(app)

    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    app.register_blueprint(users_app)
    app.register_blueprint(article)
    app.register_blueprint(auth_app, url_prefix="/auth")
