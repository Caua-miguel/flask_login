from flask import Blueprint, jsonify
from project.users.services.user_services import User

user_blueprint = Blueprint("user", __name__, template_folder="templates")

@user_blueprint.route("/user")
def user(): 
    users = User.select_users()
    return jsonify(users), 201

@user_blueprint.route("/register", methods=["POST"])
def register_user():
    user_exists = User.user_exists()   
    if user_exists:
        return jsonify({"error": "User already exists!"}), 409
    User.insert_user()
    return jsonify({'message': 'User added successfully!'}), 201

@user_blueprint.route("/user/<string:id>/update", methods=["PUT"])
def update_user(id):
    User.update_user(id)
    return jsonify({'message': 'User updated successfully!'}), 201

@user_blueprint.route("/user/<string:id>/delete", methods=["DELETE"])
def delete(id):
    User.delete_user(id)
    return jsonify({'message': 'User deleted successfully!'}), 201