import uuid
import json


class Order:
    def __init__(self, request_id, user_id):
        self.id = uuid.uuid4().hex
        self.request_id = request_id
        self.user_id = user_id

    def json(self):
        """
        json representation of the Order model
        """
        return json.dumps({
            'id': self.id,
            'request_id': self.request_id,
            'user_id': self.user_id
        })