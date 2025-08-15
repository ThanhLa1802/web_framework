import bcrypt
import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = 'secret_key_for_jwt'

class AuthService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register_user(self, username, password):
        if self.user_repository.get_user_by_username(username):
            raise ValueError("Username already exists")
        
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return self.user_repository.create(username, password_hash)
    
    def login(self, username, password):
        user = self.user_repository.get_user_by_username(username)
        if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password_hash):
            raise ValueError("Invalid username or password")
        
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.now(timezone.utc) + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm='HS256')
        
        return token