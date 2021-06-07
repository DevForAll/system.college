from flask import Flask
from flask_restful import Api
from resources.userResource import User

#   CREACION DE APP 
app = Flask(__name__)

api = Api(app)

#   AGREGANDO ENDPOINTS
api.add_resource(User, "/users")


if __name__ == '__main__':
    #   EJECUCION DE NUESTRA APP
    app.run(port=5000, debug=True)