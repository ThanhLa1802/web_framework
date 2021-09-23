from flask import Flask, request, Blueprint
from .helper.extension import ma, db
from store.product_module.routes import product
from store.category_module.routes import category
def create_app(config_file = "config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.register_blueprint(product)
    app.register_blueprint(category)
    ma.init_app(app)
    db.init_app(app)
    return app