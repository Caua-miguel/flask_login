from flask import Flask
import flask_login
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = '123'
CORS(app)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

from project.home.views import home_blueprint
from project.auth.views import login_blueprint
from project.users.views import user_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(user_blueprint)

# Importa o user_loader
from project.auth.config import login