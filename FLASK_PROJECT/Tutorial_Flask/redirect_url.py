from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1> Thanh DZ </h1>"


@app.route('/admin')
def hello_admin():
    return f"<h1> Hello admin dep trai!</h1>"


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    return f"<h1> Hello {name}!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
