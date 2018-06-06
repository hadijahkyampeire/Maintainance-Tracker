import uuid
import json


class Request:
    def __init__(self, id, title, description, department):
        self.id = id
        self.title= title
        self.description = description
        self.department = department

    def json(self):
        """
        json representation of the Order model
        """
        return json.dumps({
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'department':self.department
        })