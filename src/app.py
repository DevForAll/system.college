import os
from flask import Flask
from flask_restful import Api
from resources.userResource import User
from db import db
from dotenv import load_dotenv
from ma import ma


#   CREACION DE APP 
app = Flask(__name__)
# load_dotenv(".env")
app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost/school"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
#   AGREGANDO ENDPOINTS
api.add_resource(User, "/users")


if __name__ == '__main__':
    #   EJECUCION DE NUESTRA APP
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)