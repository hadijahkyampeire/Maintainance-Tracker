import json

from test.base import BaseTestCase


class Test_auth(BaseTestCase):
    def test_successful_signup(self):
        """
        Test a user is successfully created through the api
        """
        with self.client:
            response = self.register_user("hadijah", "had@gmail.com", "12345")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(data.get('message'), "User successfully created")
            # Add the same user and see...
            res = self.register_user("hadijah", "had@gmail.com", "12345")
            data1 = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 400)
            self.assertEqual(data1.get('message'), "email already in use")

    def test_successful_login(self):
        """
        Test a registered user  is logged in successfully through the api
        """
        with self.client:
            self.register_user("hadijah", "had@gmail.com", "12345")
            response = self.login_user("had@gmail.com", "12345")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data.get('message'),
                             "User logged in successfully")

    def test_wrong_credentials_on_login(self):
        """
        Test a user logs in with wrong credentials
        """
        with self.client:
            self.register_user("hadijah", "had@gmail.com", "12345")
            response = self.login_user("dija@gmail.com", "1234509")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertEqual(data.get('message'),
                             "wrong credentials")

    def test_invalid_username_onsignup(self):
        """Test when a user registers with an invalid username"""
        with self.client:
            response = self.register_user("h", "had@gmail.com", "12345")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data.get('message'), "invalid, Enter name please")
            
    def test_username_with_characters_onsignup(self):
        """Test when a user registers with an invalid username with characters"""
        with self.client:
            response = self.register_user("?4?5@", "had@gmail.com", "12345")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data.get('message'), "Invalid characters not allowed")

    def test_when_invalid_email_onsignup(self):
        """Test when invalid email is provided onsignup"""
        with self.client:
            response = self.register_user("hadijah", "hadgmailcom", "123456")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data.get('message'), "Enter valid email")

    def test_when_no_password_onsignup(self):
        """Test when no password onsignup"""
        with self.client:
            response = self.register_user("hadijah", "had@gmail.com", "")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data.get('message'), "Enter password")

    def test_when_short_password_onsignup(self):
        """Test when short password is provided onsignup"""
        with self.client:
            response = self.register_user("hadijah", "had@gmail.com", "123")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data.get('message'), "Password is too short, < 5")