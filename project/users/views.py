from flask import Blueprint, jsonify

user_blueprint = Blueprint("user", __name__, template_folder="templates")

@user_blueprint.route("/user", methods=['GET'])
def user():
    users = [
        {"id": "asdqwedad23412", "name": "Jefferson", "age": "34", "email": "jeff@teste.com"},
        {"id": "klmdklvmksarf2342","name": "Camila", "age": "23", "email": "cam@teste.com"},
    ]
    return jsonify(users)
