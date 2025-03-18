from flask import Blueprint, jsonify, request
from database.db import db
from database.models import User_ORM

user_blueprint = Blueprint("user", __name__, template_folder="templates")

users = db.session.query(User_ORM).all()

@user_blueprint.route("/user", methods=['GET', 'POST'])
def user():

    if request.method == 'GET':
        users_list = [user.as_dict() for user in users]
        return jsonify(users_list)
        
    data = request.get_json()
    newUser = User_ORM(name=data['name'], age=data['age'], email=data['email'])
    db.session.add(newUser)
    db.session.commit()
    return jsonify({'message': 'Usuário adicionado com sucesso!'}), 201

@user_blueprint.route("/user/<int:id>/delete", methods=["GET", "DELETE"])
def delete(id):
    user_by_id = db.get_or_404(User_ORM, id)

    if request.method == "DELETE":
        db.session.delete(user_by_id)
        db.session.commit()
        return jsonify({'message': 'Usuário deletado com sucesso!'}), 201
    return jsonify({'message': 'Method delete'}), 201