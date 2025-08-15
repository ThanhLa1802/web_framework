from core.entities.user import User
from .db import get_db_connection

class UserRepository:
    def get_user_by_username(self, username):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return User(id=row['id'], username=row['username'], password_hash=row['password_hash'])
        return None
    
    def create(self, username, password_hash):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return User(id=user_id, username=username, password_hash=password_hash)