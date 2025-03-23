from flask import Flask
import flask_login
from flask_cors import CORS
from database.config.db import AplicationConfig
from database.models.users import db
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(AplicationConfig)
bcrypt = Bcrypt(app)
CORS(app)
db.init_app(app)

migrate = Migrate(app, db)

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