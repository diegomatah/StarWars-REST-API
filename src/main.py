"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, FavPeople, Planetas, FavPlanetas
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/people', methods=['GET'])
def getPeople():

    return jsonify({
        "mensaje":"registro de base de datos depersonajes",
        "people": []
    })

@app.route('/people/<int:people_id>',methods=['GET'])
def getPeople2(people_id):
    return jsonify({
        "id": people_id,
        "mensaje": "informacion del personaje X"
    })

@app.route('/planets', methods=['GET'])
def getPlanets():

    return jsonify({
        "mensaje":"registro de base de datos de planetas",
        "planets": []
    })

@app.route('/planets/<int:planets_id>', methods=['GET'])
def getPlanets2(planets_id):

    return jsonify({
        "id": planets_id,
        "mensaje": "informacion del planeta X"
    })
 
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
