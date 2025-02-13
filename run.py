from project import app
from flask import render_template

@app.route('/')
def home():
    return "Jumbas is a pachiderm!"

@app.route('/welcome')
def welcome():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)