import flask_login
from uuid import uuid4
from database.config.db import db

def get_uuid():
    return uuid4().hex

class Users(db.Model, flask_login.UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.String(345), nullable=False)
    email = db.Column(db.String(100), nullable=False) # Tornar unico ao ajustar o login
    password = db.Column(db.Text, nullable=False)

    def as_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'email': self.email,
        }
