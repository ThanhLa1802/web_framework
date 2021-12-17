from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.config["SECRET_KEY"] = "thanhdz"
app.permanent_session_lifetime = timedelta(minutes=1)


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_name = request.form["name"]
        session.permanent = True
        if user_name:
            session["user"] = user_name
            return redirect(url_for("hello_user", name=user_name))
    if "user" in session:
        name = session["user"]
        return f"<h1> Hello {name}!</h1>"
    return render_template("login.html")


@app.route("/user")
def hello_user():
    if "user" in session:
        name = session["user"]
        return f"<h1> Hello {name}!</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def log_out():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
