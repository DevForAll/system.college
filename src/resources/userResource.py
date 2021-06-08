from flask_restful import Resource
from flask import request
from models.userModel import UserModels
from schema.userSchema import UserSchema


user_list_schema = UserSchema(many=True)

class User(Resource):
    @classmethod
    def get(cls):
        return {"users": user_list_schema.dump(UserModels.find_all_users())}, 200