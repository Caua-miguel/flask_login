from flask import Blueprint, jsonify

user_blueprint = Blueprint("user", __name__, template_folder="templates")

@user_blueprint.route("/user", methods=['GET'])
def user():
    pass