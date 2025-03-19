from flask import Blueprint, jsonify
from database.models import db
from database.models import User_ORM
from flask_login import login_required

home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/')
@login_required
def home():
    users = db.session.query(User_ORM).all()
    return jsonify({"Users: ": users})

@home_blueprint.route('/welcome')
def welcome():
    return jsonify({"Message: ": "Welcome"})

