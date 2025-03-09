from flask import Blueprint, jsonify, request, redirect, url_for, render_template
from database.db import db
from database.models import User_ORM

user_blueprint = Blueprint("user", __name__, template_folder="templates")



@user_blueprint.route("/user", methods=['GET', 'POST'])
def user():

    if request.method == 'GET':
        users = db.session.query(User_ORM).all()
        users_list = [user.as_dict() for user in users]
        return jsonify(users_list)
        
    data = request.get_json()
    newUser = User_ORM(name=data['name'], age=data['age'], email=data['email'])
    db.session.add(newUser)
    db.session.commit()
    return jsonify({'message': 'Usuário adicionado com sucesso!'}), 201

@user_blueprint.route("/user/<int:id>/delete", methods=["GET", "POST"])
def delete(id):
    user_by_id = db.get_or_404(User_ORM, id)

    if request.method == "POST":
        db.session.delete(user_by_id)
        db.session.commit()
        return redirect(url_for("home.home"))
    return render_template("delete.html", user_by_id=user_by_id)