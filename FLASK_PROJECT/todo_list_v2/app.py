from flask import Flask
from flask_cors import CORS
from interface.todo_controller import todo_blueprint
from interface.auth_controller import auth_blueprint
from infrastructure.db import initialize_db


app = Flask(__name__)
CORS(app)

initialize_db()  # Initialize the database connection

app.register_blueprint(todo_blueprint, url_prefix='/api')
app.register_blueprint(auth_blueprint, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)