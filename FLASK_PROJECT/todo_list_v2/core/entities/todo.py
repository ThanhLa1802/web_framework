class Todo:
    def __init__(self, user_id, title, description, completed=False, id=None):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }