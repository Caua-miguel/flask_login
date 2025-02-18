from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = '123'

login_manager = LoginManager()
login_manager.init_app(app)

# Importa o user_loader
from project.auth.config import login