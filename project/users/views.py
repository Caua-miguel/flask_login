from flask import Blueprint, jsonify, request
from database.db import db
from database.models import User_ORM

user_blueprint = Blueprint("user", __name__, template_folder="templates")

@user_blueprint.route("/user", methods=['GET', 'POST'])
def user():

    if request.method == 'GET':
        users = db.session.query(User_ORM).all()
        for user in users:
           return jsonify(user.name, user.age, user.email)
        

    data = request.get_json()
    newUser = User_ORM(name=data['name'], age=data['age'], email=data['email'])
    db.session.add(newUser)
    db.session.commit()
    return jsonify({'message': 'Usuário adicionado com sucesso!'}), 201