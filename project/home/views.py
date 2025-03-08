from flask import Blueprint, render_template
from database.db import db
from database.models import User_ORM
from flask_login import login_required

home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/')
@login_required
def home():
    users = db.session.query(User_ORM).all()
    return render_template("index.html", users=users)

@home_blueprint.route('/welcome')
def welcome():
    return render_template('base.html')

