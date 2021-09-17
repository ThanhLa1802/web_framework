from flask import Flask, request, jsonify, Blueprint
from .routes import routes
from .extension import db, ma
def create_app(config_file = "settings.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.register_blueprint(routes)
    ma.init_app(app)
    db.init_app(app)
    return app



