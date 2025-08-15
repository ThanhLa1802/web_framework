from core.entities.todo import Todo
from .db import get_db_connection

class TodoRepository:
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM todos')
        rows = cursor.fetchall()
        conn.close()
        return [Todo(id=row['id'], user_id=row['user_id'], title=row['title'], description=row['description'], completed=row['completed']) for row in rows]

    def get_by_id(self, todo_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM todos WHERE id = ?', (todo_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Todo(id=row['id'], user_id=row['user_id'], title=row['title'], description=row['description'], completed=row['completed'])
        return None

    def create(self, todo_data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO todos (user_id, title, description, completed) VALUES (?, ?, ?, ?)', 
                       (todo_data.user_id, todo_data.title, todo_data.description, todo_data.completed))
        conn.commit()
        todo_id = cursor.lastrowid
        conn.close()
        return Todo(id=todo_id, user_id=todo_data.user_id, title=todo_data.title, description=todo_data.description, completed=todo_data.completed)

    def update(self, todo_id, todo_data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE todos SET title = ?, description = ?, completed = ? WHERE id = ?', 
                       (todo_data.title, todo_data.description, todo_data.completed, todo_id))
        conn.commit()
        conn.close()

    def delete(self, todo_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
        conn.commit()
        conn.close()