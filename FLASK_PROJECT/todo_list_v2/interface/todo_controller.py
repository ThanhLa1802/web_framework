from flask import Blueprint, request, jsonify
from core.use_cases.todo_services import TodoServices
from infrastructure.todo_repo import TodoRepository
from core.use_cases.auth_services import SECRET_KEY
from core.entities.todo import Todo
import jwt

todo_blueprint = Blueprint('todo', __name__)
todo_service = TodoServices(TodoRepository())

@todo_blueprint.route('/todos', methods=['GET'])
def get_all_todos():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Authorization token is required'}), 401
    
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

    todos = todo_service.get_all_todos()
    return jsonify([todo.__dict__ for todo in todos]), 200

@todo_blueprint.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo_by_id(todo_id):
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Authorization token is required'}), 401
    
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

    todo = todo_service.get_todo_by_id(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    
    return jsonify(todo.__dict__), 200

@todo_blueprint.route('/todos', methods=['POST'])
def create_todo():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Authorization token is required'}), 401
    
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

    data = request.get_json()
    user_id = data.get('user_id')
    title = data.get('title')
    description = data.get('description', '')
    completed = data.get('completed', False)

    if not user_id or not title:
        return jsonify({'error': 'User ID and title are required'}), 400

    todo_data = Todo(user_id=user_id, title=title, description=description, completed=completed)
    todo = todo_service.create_todo(todo_data)
    
    return jsonify(todo.__dict__), 201

@todo_blueprint.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Authorization token is required'}), 401
    
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

    data = request.get_json()
    title = data.get('title')
    description = data.get('description', '')
    completed = data.get('completed', False)

    if not title:
        return jsonify({'error': 'Title is required'}), 400

    todo_data = Todo(id=todo_id, title=title, description=description, completed=completed)
    todo_service.update_todo(todo_id, todo_data)
    
    return jsonify({'message': 'Todo updated successfully'}), 200

@todo_blueprint.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Authorization token is required'}), 401
    
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

    todo_service.delete_todo(todo_id)
    
    return jsonify({'message': 'Todo deleted successfully'}), 200
