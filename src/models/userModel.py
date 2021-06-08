from typing import List

from sqlalchemy.orm import query
from db import db

class UserModels(db.Model):
    __tablename__ = "tpp_usuario"
    in_idusuario = db.Column(db.Integer, primary_key=True)
    vc_nombre = db.Column(db.String)
    vc_apellido_parterno = db.Column(db.String)
    vc_apellido_materno = db.Column(db.String)
    vc_codigo = db.Column(db.String)
    vc_usuario = db.Column(db.String)
    vc_password = db.Column(db.String)
    in_tipo_documento = db.Column(db.Integer)
    dt_nacimiento = db.Column(db.Date)
    vc_pais = db.Column(db.String)
    vc_departamento = db.Column(db.String)
    vc_provincia = db.Column(db.String)
    vc_distrito = db.Column(db.String)
    vc_direccion = db.Column(db.String)
    dt_registry = db.Column(db.DateTime)
    vc_celular = db.Column(db.String)
    vc_correo = db.Column(db.String)

    @classmethod
    def find_all_users(cls) -> List["UserModels"]:
        return cls.query.all()