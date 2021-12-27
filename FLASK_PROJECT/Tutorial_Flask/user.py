from flask import Flask, redirect, url_for, render_template, request, session
from flask.helpers import flash
from flask import Blueprint

user = Blueprint("user", __name__)


@user.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_name = request.form["name"]
        session.permanent = True
        if user_name:
            session["user"] = user_name
            return redirect(url_for("user.user_name", user=user_name))
    if "user" in session:
        name = session["user"]
        return redirect(url_for("user.user_name", user=user_name))
    return render_template("login.html")


@user.route("/user")
def user_name():
    if "user" in session:
        name = session["user"]
        return render_template("user.html", user=name)
    else:
        return redirect(url_for("user.login"))


@user.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("user.login"))
