from dotenv import load_dotenv
import redis
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

load_dotenv()

class AplicationConfig:
    SECRET_KEY = os.environ['SECRET_KEY']

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = r"sqlite:///./db.sqlite"

    SESSION_TYPE = "redis"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")
