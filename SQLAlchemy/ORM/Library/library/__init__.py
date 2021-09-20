from flask import Flask, request, Blueprint
from library.student.routes import student
from library.book.routes import book
from library.author_category.routes import author_cat
from .extension import db, ma 
def create_app(config_file = "config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.register_blueprint(student)
    app.register_blueprint(book)
    app.register_blueprint(author_cat)
    ma.init_app(app)
    db.init_app(app)
    return app