from flask import Blueprint, request, jsonify
from core.use_cases.auth_services import AuthService
from infrastructure.user_repo import UserRepository

auth_blueprint = Blueprint('auth', __name__)
auth_service = AuthService(UserRepository())

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    
    try:
        user = auth_service.register_user(username, password)
        return jsonify({'id': user.id, 'username': user.username}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    
    try:
        token = auth_service.login(username, password)
        return jsonify({'token': token}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 401

