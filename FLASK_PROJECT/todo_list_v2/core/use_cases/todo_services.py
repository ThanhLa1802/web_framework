class TodoServices:
    def __init__(self, todo_repository):
        self.todo_repository = todo_repository

    def get_all_todos(self):
        return self.todo_repository.get_all()

    def get_todo_by_id(self, todo_id):
        return self.todo_repository.get_by_id(todo_id)

    def create_todo(self, todo_data):
        return self.todo_repository.create(todo_data)

    def update_todo(self, todo_id, todo_data):
        return self.todo_repository.update(todo_id, todo_data)

    def delete_todo(self, todo_id):
        return self.todo_repository.delete(todo_id)