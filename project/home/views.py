from flask import Blueprint, render_template, g
import flask_login
import sqlite3
import os

home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/')
@flask_login.login_required
def home():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('index.html', posts=posts)

@home_blueprint.route('/welcome')
def welcome():
    return render_template('base.html')

def connect_db():
    db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'database', 'storage', 'sample.db')
    return sqlite3.connect(db_path)

