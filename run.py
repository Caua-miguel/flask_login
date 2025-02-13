
from flask import Flask, render_template, request, url_for, redirect
from jinja2 import FileSystemLoader
import os

app = Flask(__name__)

template_dirs = [os.path.join(os.path.dirname(__file__), 'project', 'users', 'templates'),
                 os.path.join(os.path.dirname(__file__), 'project', 'templates')]

app.jinja_loader = FileSystemLoader(template_dirs)

@app.route('/')
def home():
    return "Jumbas is a pachiderm!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials! Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/welcome')
def welcome():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)