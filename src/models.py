from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    uid = db.Column(db.Integer,primary_key=True)
    name = db.Column (db.String(80), unique = False, nullable = False)
    homeworld = db.Column (db.String(250), unique = True, nullable = True)

    def __repr__(self):
           return '<People %r>' %self.name

    def serialize(self):
        return{
            "uid": self.uid,
            "name": self.name,
            "homeworld": self.homeworld
        }

class FavPeople(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(120), db.ForeignKey("user.email"))
    people = db.Column(db.Integer, db.ForeignKey("people.uid"))
    rel_user = db.relationship('User') 
    rel_people = db.relationship('People')

    def __repr__(self):
           return '<FavPeople %r>' %self.id

    def serialize(self):
        return{
            "id": self.id,
            "user": self.user,
            "people": self.people,
        }

class Planetas(db.Model):
    uid = db.Column(db.Integer,primary_key=True)
    name = db.Column (db.String(80), unique = True, nullable = False)

    def __repr__(self):
            return '<Planetas %r>' %self.name

    def serialize(self):
            return{
                "uid": self.uid,
                "name": self.name,
            }

class FavPlanetas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(120), db.ForeignKey("user.email"))
    planetas = db.Column(db.String(80), db.ForeignKey("planetas.name"))
    rel_user = db.relationship('User') 
    rel_planetas = db.relationship('Planetas')

    def __repr__(self):
           return '<FavPlanetas %r>' %self.id

    def serialize(self):
        return{
            "id": self.id,
            "user": self.user,
            "planetas": self.planetas,
        }