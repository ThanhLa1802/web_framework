from flask import Flask, request, Blueprint
from .books.controller import books
from .borrow.controller import borrow
from .extension import db, ma
from .model import Students, Books, Author, Category, Borrows
import os


def create_db(app):
    if not os.path.exists("library/library.db"):
        with app.app_context():
            db.create_all()
            print("Created DB!")


def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    ma.init_app(app)
    create_db(app)
    app.register_blueprint(books)
    app.register_blueprint(borrow)
    return app
