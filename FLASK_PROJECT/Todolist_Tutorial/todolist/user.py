from re import template
from flask import Blueprint, render_template

user = Blueprint("user", __name__)


@user.route("/login")
def login():
    return render_template("login.html")


@user.route("/signup")
def signup():
    return render_template("signup.html")


@user.route("/logout")
def logout():
    return "Logout Page"
