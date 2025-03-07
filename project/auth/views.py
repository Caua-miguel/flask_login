from flask import Blueprint, request, render_template, redirect, url_for
from database.models import users, User
import flask_login

login_blueprint = Blueprint('login', __name__, template_folder='templates')

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
            return render_template('login.html')
    
    username = request.form['username']

    if username in users and request.form['password'] == users[username]['password']:
        user = User()
        user.id = username
        flask_login.login_user(user)
        print("Login: " + username + " Senha:"+ request.form['password'])
        return redirect(url_for('login.protected'))

    return 'Bad login'
    
@login_blueprint.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@login_blueprint.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'