from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
from user import user

app = Flask(__name__)
app.config["SECRET_KEY"] = "thanhdz"
app.permanent_session_lifetime = timedelta(minutes=1)
app.register_blueprint(user, url_prefix="/user")


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
