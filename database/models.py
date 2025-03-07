import flask_login

users = {'admin': {'password': 'admin'}}

class User(flask_login.UserMixin):
    pass

from sqlalchemy.dialects.sqlite import INTEGER
from database.db import db

class User_ORM(db.Model):
    __tablename__ = 'user_orm'

    id = db.Column(INTEGER(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(INTEGER(), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def as_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'email': self.email
        }
