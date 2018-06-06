import json

from .base import BaseTestCase

class Tests_Requests(BaseTestCase):
    """Test for requests"""
    def test_add_request_successfully(self):
        """Tests when the requests are submitted successfully"""
        with self.client:
            self.register_user("hadijah", "had@gmail.com", "12345")
            token = self.get_token()
            response = self.add_request(token)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(data.get('message'), "Request successfully created and sent")
            res = self.add_request(self.get_token())
            data1 = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 400)
            self.assertEqual(data1.get('message'), "Request title already exists")

    def test_get_all_requests(self):
        """Tests when all requests are retrieved successfully"""
        with self.client:
            self.register_user("hadijah", "had@gmail.com", "12345")
            token = self.get_token()
            self.add_request(token)
            response = self.get_requests(token)
            self.assertEqual(response.status_code, 200)

    def test_add_request_with_no_token(self):
        """Tests when the requests are submitted successfully"""
        with self.client:
            self.register_user("hadijah", "had@gmail.com", "12345")
            token = ""
            response = self.add_request(token)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertEqual(data.get('message'), "Token is missing")

    def test_gets_all_requests_with_no_token(self):
        """Tests when the requests are submitted successfully"""
        with self.client:
            self.register_user("hadijah", "had@gmail.com", "12345")
            token = ""
            response = self.get_requests(token)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertEqual(data.get('message'), "Token is missing")
    # def test_get_one_request(self):
    #     """Tests when one request is retrieved successfully"""
    #     with self.client:
    #         self.register_user("hadijah", "had@gmail.com", "12345")
    #         token = self.get_token()
    #         self.add_request(token)
    #         response = self.get_one_request(token)
    #         self.assertEqual(response.status_code, 200)

    # def test_edit_request(self):
    #     """Tests when one request is edited successfully"""
    #     with self.client:
    #         self.register_user("hadijah", "had@gmail.com", "12345")
    #         token = self.get_token()
    #         self.add_request(token)
    #         response = self.put_request(token)
    #         self.assertEqual(response.status_code, 200)