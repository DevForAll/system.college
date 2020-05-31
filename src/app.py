from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#	CREACION DE APLICACION Y CONFIGURACION DE SQL
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@127.0.0.1:3306/college?charset=utf8mb4' # CADENA DE CONEXION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)	#	DEVUELVE LA INSTANCIA DE BASE DE DATOS
ma = Marshmallow(app)	#	DEBUELVE EL ESQUEMA DE LA BASE DE DATOS

#######################################################################################################
#	TODA ESTA CLASE CREARA UNA TABLE EN LA BASE DE DATOS
class Task(db.Model):	#	SE CREA LA CLASE TASK , HEREDA DEL MODELO DE LA BASE DE DATOS (las tablas )
	id = db.Column(db.Integer, primary_key=True)	#SE IMPORTA "CLOMUN" EÑ TIPO DE DATO Y LA LONGITUD
	name = db.Column(db.String(70), unique=True)
	last_name = db.Column(db.String(70))
	active = db.Column(db.Integer)

	def __init__(self, name, last_name, active):	# SE EJECUTA CADA VEZ QUE SE INSTANCIA ESA CLASE
		self.name = name
		self.last_name = last_name
		self.active = active

# db.create_all()	#que indica a la aplicación que cree todas las tablas y bases de datos especificadas en la aplicación
#######################################################################################################
class TaskSchema(ma.Schema):	
	class Meta:
		fields = ('id', 'name', 'last_name', 'active')	#CAMPOS QUE SE QUIEREN OBTENER PARA INTERACTUAR CON EL SQUEMA

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
#######################################################################################################
class ttp_test(db.Model):
	IN_IDTEST = db.Column(db.Integer, nullable=False, primary_key=True)
	VC_GAME = db.Column(db.String(50), nullable=False)
	VC_TYPE = db.Column(db.String(50), nullable=False)
	IN_ACTIVE = db.Column(db.Integer, nullable=False)

	def __init__(self, VC_GAME, VC_TYPE, IN_ACTIVE ):
		self.VC_GAME = VC_GAME
		self.VC_TYPE = VC_TYPE
		self.IN_ACTIVE = IN_ACTIVE
	# def __repr__(self):
	# 	return '' % self.IN_IDTEST
class ttp_testSchema(ma.Schema):
	class Metas:
		campos = ('IN_IDTEST','VC_GAME', 'VC_TYPE', 'IN_ACTIVE')

test_schema = ttp_testSchema()
tests_schema = ttp_testSchema(many=True)
#######################################################################################################
#	CREACION DE ENDPOINTs
@app.route('/tests', methods=['GET'])
def get_tests():
	all_tests = ttp_test.query.all()
	result = tests_schema.jsonify(all_tests)
	return result

@app.route('/user', methods=['POST'])
def create_user():
	name = request.json['name']
	last_name = request.json['last_name']
	active = request.json['active']

	new_user = Task(name, last_name, active)
	db.session.add(new_user)
	db.session.commit()
 
	return task_schema.jsonify(new_user)

@app.route('/users', methods=['GET'])
def get_users():
	all_tasks = Task.query.all()
	result = tasks_schema.jsonify(all_tasks)
	return result

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
	user = Task.query.get(id)
	result = task_schema.dump(user)
	return result

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
	user = Task.query.get(id)
	name = request.json['name']
	last_name = request.json['last_name']
	active = request.json['active']

	user.name = name
	user.last_name = last_name
	user.active = active

	db.session.commit()
	return task_schema.jsonify(user)

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
	user = Task.query.get(id)
	db.session.delete(user)
	db.session.commit()

	return task_schema.jsonify(user)

@app.route('/', methods=['GET'])
def index():
	return jsonify({'message': 'Welcome to my API MGSP'})

if __name__ == "__main__":
    app.run(debug=True)