
from flask import Flask, render_template, request, url_for, redirect, session, flash
from jinja2 import FileSystemLoader
from functools import wraps
import os

app = Flask(__name__)

app.secret_key = "123"

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

template_dirs = [os.path.join(os.path.dirname(__file__), 'project', 'users', 'templates'),
                 os.path.join(os.path.dirname(__file__), 'project', 'templates')]

app.jinja_loader = FileSystemLoader(template_dirs)

@app.route('/')
@login_required
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials! Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)