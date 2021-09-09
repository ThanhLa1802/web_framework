
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_dance.contrib.github import make_github_blueprint, github
app = Flask(__name__)
app.secret_key = "0dcea6a90267ed0040313a4616b3a15e"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category ='info'

blueprint = make_github_blueprint(
    client_id="9cc07b32d6aacf29d4b4",
    client_secret="d7b4f3655831ff69f13d0684e6c0eea7a724a359",
)
app.register_blueprint(blueprint, url_prefix="/login")
from flaskblog import routes