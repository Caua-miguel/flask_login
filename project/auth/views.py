from flask import Blueprint, request, jsonify
from database.models import User_ORM
import flask_login
# from project import bcrypt

login_blueprint = Blueprint('login', __name__, template_folder='templates')

# @login_blueprint.route('/login', methods=['GET', 'POST'])
# def login():

#     email = request.json["email"]
#     password = request.json["password"]

#     user = User_ORM.query.filter_by(email=email).first()

#     if user is None:
#         return jsonify({"error": "Unauthorized"}), 401
    
#     if not bcrypt.check_password_hash(user.password, password):
#         return jsonify({"error": "Unauthorized"}), 401
    
#     user.id = email

#     flask_login.login_user(user)

#     return jsonify({
#         "id": user.id,
#         "email": user.email
#     })
    
@login_blueprint.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@login_blueprint.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'