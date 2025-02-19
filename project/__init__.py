from flask import Flask
import flask_login

app = Flask(__name__)
app.secret_key = '123'

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

from project.home.views import home_blueprint
from project.auth.views import login_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(login_blueprint)

# Importa o user_loader
from project.auth.config import login