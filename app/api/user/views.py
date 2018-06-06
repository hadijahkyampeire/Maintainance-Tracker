from flask import jsonify, make_response
from flask_restful import Resource, reqparse

import re
import json

from app.api.models.users import User, generate_token

users_list = []

class Signup(Resource):
    def post(self):
        """
        Allows users(admins and customers) to create accounts
        """

        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)

        args = parser.parse_args()
        username = args['username']
        email = args['email']
        password = args['password']

        if username.strip() == "" or len(username.strip()) < 2:
            return make_response(jsonify({"message": "invalid, Enter name please"}), 400)

        if re.compile('[!@#$%^&*:;?><.0-9]').match(username):
            return make_response(jsonify({"message": "Invalid characters not allowed"}), 400)

        if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
            return make_response(jsonify({"message": "Enter valid email"}), 400)

        if password.strip() == "":
            return make_response(jsonify({"message": "Enter password"}), 400)

        if len(password) < 5:
            return make_response(jsonify({"message": "Password is too short, < 5"}), 400)

        new_user = User(username, email, password)

        for user in users_list:
            if email == user['email']:
                return make_response(jsonify({"message": "email already in use"}), 400)

        users_list.append(json.loads(new_user.json()))
        return make_response(jsonify({'message': 'User successfully created', 'email': new_user.email}), 201)

class Login(Resource):
    def post(self):
        """
        Allows users to login to their accounts
        """
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)

        args = parser.parse_args()
        email = args['email']
        password = args['password']

        for user in users_list:
            if email == user['email'] and password == user['password']:
                access_token = "{}".format(
                    generate_token(user['id']))
                return make_response(jsonify({"token": access_token,
                                              "message": "User logged in successfully"
                                              }), 200)
        return make_response(jsonify({"message": "wrong credentials"}), 401)

# class AdminLogin(Resource):
#     def post(self):
#         """
#         Allows users to login to their accounts
#         """
#         parser = reqparse.RequestParser()
#         parser.add_argument('username', type=str, required=True)
#         parser.add_argument('password', type=str, required=True)

#         args = parser.parse_args()
#         username = args['username']
#         password = args['password']

#         for user in users_list:
#             if username == user['admin'] and password == user['Admin123']:
#                 access_token = "{}".format(
#                     generate_token(user['id']))
#                 return make_response(jsonify({"token": access_token,
#                                               "message": "User logged in successfully"
#                                               }), 200)
#         return make_response(jsonify({"message": "wrong credentials"}), 401)

