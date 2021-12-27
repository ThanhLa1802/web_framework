from enum import EnumMeta
from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
app.config["SECRET_KEY"] = "thanhdz"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=1)

db = SQLAlchemy(app)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_name = request.form["name"]
        session.permanent = True
        if user_name:
            session["user"] = user_name
            found_user = User.query.filter_by(name=user_name).first()
            if found_user:
                session["email"] = found_user.email
            else:
                user = User(user_name, "temp@gmail.com")
                db.session.add(user)
                db.session.commit()
                flash("Created in DB!")
            return redirect(url_for("user", user=user_name))
    if "user" in session:
        name = session["user"]
        return redirect(url_for("user", user=user_name))
    return render_template("login.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        name = session["user"]
        if request.method == "POST":
            if not request.form["email"] and request.form["name"]:
                User.query.filter_by(name=name).delete()
                db.session.commit()
                flash("Deleted user!")
                return redirect(url_for("log_out"))
            else:
                email = request.form["email"]
                session["email"] = email
                found_user = User.query.filter_by(name=name).first()
                found_user.email = email
                db.session.commit()
                flash("Email updated!")
        elif "email" in session:
            email = session["email"]
        return render_template("user.html", user=name, email=email)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def log_out():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    if not path.exists("user.db"):
        db.create_all(app=app)
        print("Created database!")
    app.run(debug=True)
