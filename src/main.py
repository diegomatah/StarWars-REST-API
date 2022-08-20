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
    all_people = People.query.all()
    serializados = list( map( lambda people: people.serialize(), all_people))
    return jsonify({
        "mensaje":"registro de base de datos depersonajes",
        "people": serializados
    }), 200

@app.route('/onePeople/<int:people_id>',methods=['GET'])
def onePeople(people_id):
    one = People.query.filter_by(uid=people_id).first()
    if (one):
     return jsonify({
        "id": people_id,
        "mensaje": "informacion del personaje",
        "people": one.serialize()
    })
    else:
        return jsonify({
            "id":people_id,
            "mensaje": "not found"
        }),404

@app.route('/planetas', methods=['GET'])
def getPlanetas():
    all_planets = Planetas.query.all()
    serializados2 = list( map( lambda planetas: planetas.serialize(), all_planets))
    return jsonify({
        "mensaje":"registro de base de datos de planetas",
        "planets": serializados2
    }), 200

@app.route('/onePlanet/<int:planets_id>', methods=['GET'])
def onePlanet(planets_id):
    onePlaneta = Planetas.query.filter_by(uid=planets_id).first()
    if(onePlaneta):
     return jsonify({
        "id": planets_id,
        "mensaje": "informacion del planeta",
        "planetas": onePlaneta.serialize()
    })
    else:
        return jsonify({
            "id":planets_id,
            "mensaje": "not found"
        }),404

@app.route("/favorite/people/<int:people_id>", methods = ['POST'])
def postPeopleFav(people_id):
    body = request.get_json()
    newFav = FavPeople(user=body['email'], people=people_id)
    db.session.add(newFav)
    db.session.commit()
    return "nuevo favorito agregado"

@app.route("/favorite/planetas/<int:planets_id>", methods = ['POST'])
def postPlanetsFav(planets_id):
    bodyplanet = request.get_json()
    newFavplanet = FavPlanetas(user=bodyplanet['email'], planetas=planets_id)
    db.session.add(newFavplanet)
    db.session.commit()
    return "nuevo planeta favorito agregado"
 
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
