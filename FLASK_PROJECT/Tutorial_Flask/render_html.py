from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', content="Thanh dep trai!",
                           cars=["Vinfast", "BMW", "Mer"])


if __name__ == "__main__":
    app.run(debug=True)
