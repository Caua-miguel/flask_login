from flask import Blueprint, jsonify, request
from project import bcrypt
from database.models import db
from database.models import User_ORM

user_blueprint = Blueprint("user", __name__, template_folder="templates")

@user_blueprint.route("/user", methods=['GET', 'POST'])
def user():

    if request.method == 'GET':
        users = db.session.query(User_ORM).all()
        users_list = [user.as_dict() for user in users]
        return jsonify(users_list)
    
    data = request.get_json()
    password = data['password']  
    
    user_exists = User_ORM.query.filter_by(email=data['email']).first() is not None    
    
    if user_exists:
        return jsonify({"error": "User already exists!"}), 409
    hash_password = bcrypt.generate_password_hash(password)
    newUser = User_ORM(name=data['name'], age=data['age'], email=data['email'], password=hash_password)
    db.session.add(newUser)
    db.session.commit()
    return jsonify({'message': 'Usuário adicionado com sucesso!'}), 201

@user_blueprint.route("/user/<string:id>/update", methods=["PUT"])
def update_user(id):
    
    data = request.get_json() 
    User_ORM.query.filter_by(id=id).update(data)
    db.session.commit()

    return jsonify({'message': 'Usuário atualizado com sucesso!'}), 201
    

@user_blueprint.route("/user/<string:id>/delete", methods=["GET", "DELETE"])
def delete(id):
    user_by_id = db.get_or_404(User_ORM, id)

    if request.method == "DELETE":
        db.session.delete(user_by_id)
        db.session.commit()
        return jsonify({'message': 'Usuário deletado com sucesso!'}), 201
    return jsonify({'message': 'Method delete'}), 201