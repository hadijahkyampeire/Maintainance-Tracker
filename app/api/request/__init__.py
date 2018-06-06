from flask import Blueprint
from flask_restful import Api
from .views import AddRequest, EditRequest, GetRequests, GetOneRequest

request = Blueprint('requests', __name__)
maintainance_api = Api(request)
maintainance_api.add_resource(AddRequest, '/api/v1/users/requests')
maintainance_api.add_resource(GetRequests, '/api/v1/users/requests')
maintainance_api.add_resource(GetOneRequest, '/api/v1/users/requests/<request_id>')
maintainance_api.add_resource(EditRequest, '/api/v1/users/requests/<request_id>')
