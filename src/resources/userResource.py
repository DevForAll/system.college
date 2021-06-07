from flask_restful import Resource
from flask import request


class User(Resource):
    @classmethod
    def get(cls):
        return {"message":"Hello world, Usuarios"}, 200