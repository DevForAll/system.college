from flask_sqlalchemy import model
from marshmallow_sqlalchemy import load_instance_mixin
from ma import ma
from models.userModel import UserModels


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModels #   AL CREAR LA VARIABLE "model" ESTAMOS VINCULANDO CON USERMODEL
        dump_only = ("id",)
        load_instance = True # Opcional: deserializar para modelar instancias