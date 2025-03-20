from flask import Blueprint, jsonify
from flask_login import login_required

home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/')
@login_required
def home():
    return jsonify({"Message: ": "Home"})

@home_blueprint.route('/welcome')
def welcome():
    return jsonify({"Message: ": "Welcome"})

