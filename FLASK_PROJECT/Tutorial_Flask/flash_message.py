from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta


app = Flask(__name__)
app.config["SECRET_KEY"] = "thanhdz"
app.permanent_session_lifetime = timedelta(minutes=1)


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
            flash("You logged in successfully!", "info")
            return render_template("user.html", user=user_name)
    if "user" in session:
        name = session["user"]
        flash("You have already logged in!", "info")
        return render_template("user.html", user=name)
    return render_template("login.html")


@app.route("/user")
def hello_user():
    if "user" in session:
        name = session["user"]
        return render_template("user.html", user=name)
    else:
        flash("You haven't logged in!", "info")
        return redirect(url_for("login"))


@app.route("/logout")
def log_out():
    flash("You logged out!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
