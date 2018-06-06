from flask import jsonify, make_response
from flask_restful import Resource, reqparse

import re
import json

from app.api.models.requests import Request
from app.api.user.views import users_list

from app.api.models.users import decode_token


request_list=[]
class AddRequest(Resource):
    id=0
    def post(self):
        """
        Allows authenticated user to make an request from the menu
        token is required to get user Id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('department', type=str, required=True)
        parser.add_argument('token', location='headers')
        args = parser.parse_args()
        if not args['token']:
            return make_response(jsonify({"message": "Token is missing"}), 401)
        decoded = decode_token(args['token'])
        if decoded["status"] == "Failure":
            return make_response(jsonify({"message": decoded["message"]}), 400)

        for user in users_list:
            if user['id'] == decoded['id']:
                title = args['title']
                description = args['description']
                department= args['department']
                if title.strip() == "" or len(title.strip()) < 2:
                    return make_response(jsonify({"message": "invalid, Enter title please"}), 401)

                if re.compile('[!@#$%^&*:;?><.0-9]').match(title):
                    return make_response(jsonify({"message": "Invalid characters not allowed"}), 401)
                
                global id
                if len(request_list)==0:
                    id = len(request_list)+1
                else:
                    id = id+1

                new_request = Request(id, title, description, department)

                for request in request_list:
                    if title == request['title']:
                        return make_response(jsonify({"message": 'Request title already exists'}), 400)
                request = json.loads(new_request.json())
                request_list.append(request)
                return make_response(jsonify({
                    'message': 'Request successfully created and sent',
                    'status': 'success'},
                ), 201)
            return make_response(jsonify({"message": "User can not send request"}), 401)
        return make_response(jsonify({"message": "Doesn't exist, Create an account please"}), 401)


class EditRequest(Resource):
    def put(self, request_id):
        """
        Returns an request made by authenticated user
        token is required to get user Id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('token', location='headers')
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('department', type=str, required=True)
        args = parser.parse_args()
        if not args['token']:
            return make_response(jsonify({"message": "Token is missing"}), 400)
        decoded = decode_token(args['token'])
        if decoded["status"] == "Failure":
            return make_response(jsonify({"message": decoded["message"]}), 400)

        for request in request_list:
            if int(request['id']) == int(request_id):
                if request["user_id"] == decoded["id"]:
                    args = parser.parse_args()
                    request['title'] = args['title']
                    request['description'] = args['description']
                    request['department'] = args['department']
                    return make_response(jsonify({"message": "request updated succesfully"}), 200)
                return make_response(jsonify({"message": "You can not update that request"}), 401)
        return make_response(jsonify({"message": "request not found"}), 404)


class GetRequests(Resource):
    def get(self):
        """
        Returns all requests made for authenticated admin
        token is required to get admin id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('token', location='headers')
        args = parser.parse_args()
        if not args['token']:
            return make_response(jsonify({"message": "Token is missing"}), 401)
        decoded = decode_token(args['token'])
        if decoded["status"] == "Failure":
            return make_response(jsonify({"message": decoded["message"]}), 400)
        my_requests = []
        for request in request_list:
            requests_data = {
                    "id": request["id"],
                    "title": request['title'],
                    "description": request['description'],
                    "department": request['department']
                }
            my_requests.append(requests_data)
        if my_requests:
            return make_response(jsonify({"requests": my_requests,
                                    "status": "success"}), 200)
        return make_response(jsonify({"message": "No requests found"}), 404)


class GetOneRequest(Resource):
    def get(self, request_id):
        """
        Returns all requests made for authenticated admin
        token is required to get admin id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('token', location='headers')
        args = parser.parse_args()
        if not args['token']:
            return make_response(jsonify({"message": "Token is missing"}), 400)
        decoded = decode_token(args['token'])
        if decoded["status"] == "Failure":
            return make_response(jsonify({"message": decoded["message"]}), 400)
        for request in request_list:
            if int(request['id']) == int(request_id):
                requests_data = {
                        "id": request["id"],
                        "title": request['title'],
                        "description": request['description'],
                        "department": request['department']
                    }
                return make_response(jsonify({"requests": requests_data,
                                    "status": "success"}), 200)
        return make_response(jsonify({"message": "No requests found"}), 404)
