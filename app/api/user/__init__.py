from flask import Blueprint
from flask_restful import Api
from .views import Signup, Login

user = Blueprint('users', __name__)

maintainance_api = Api(user)
maintainance_api.add_resource(Signup, '/api/v1/auth/signup')
maintainance_api.add_resource(Login, '/api/v1/auth/login')
# maintainance_api.add_resource(AdminLogin, '/api/v1/auth/admin/login')
