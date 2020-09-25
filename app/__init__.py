from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import environ 
from flask_redis import Redis

app = Flask(__name__)
CORS(app)
redis = Redis(app)

app.config['SQLALCHEMY_DATABASE_URI'] =  environ.get('DBURL')
SECRET = environ.get('SECRET')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import views

class UserModel(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __repr__(self):
        return f"<User {self.login}>"