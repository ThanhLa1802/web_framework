from flask import Flask
import os
from dotenv import load_dotenv
from flask_login import LoginManager, login_manager
from flask_login.utils import logout_user
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

db = SQLAlchemy()

load_dotenv()
SECRET_KEY = os.environ.get("KEY")
DB_NAME = os.environ.get("DB_NAME")


def create_database(app):
    if not os.path.exists("todolist/" + DB_NAME):
        db.create_all(app=app)
        print("Created DB!")


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .models import Note, User

    create_database(app)
    from .user import user
    from .views import views

    app.register_blueprint(user)
    app.register_blueprint(views)

    login_manager = LoginManager()
    login_manager.login_view = "user.login"
    login_manager.init_app(app)
    app.permanent_session_lifetime = timedelta(minutes=1)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
