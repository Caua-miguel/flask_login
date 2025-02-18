
from flask import render_template, url_for, redirect, request
from project import app
import flask_login
from project.models import users, User
from jinja2 import FileSystemLoader
import os

template_dirs = [os.path.join(os.path.dirname(__file__), 'project', 'auth', 'templates'),
                 os.path.join(os.path.dirname(__file__), 'project', 'templates')]

app.jinja_loader = FileSystemLoader(template_dirs)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
            return render_template('login.html')
    
    username = request.form['username']

    if username in users and request.form['password'] == users[username]['password']:
        user = User()
        user.id = username
        flask_login.login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'
    
@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

if __name__ == '__main__':
    app.run(debug=True)