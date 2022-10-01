from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from api.login import login_blueprint
from api.resources.user import User
from api.resources.message import Message
from api.resources.emotion import Emotion

app.register_blueprint(login_blueprint)
api.add_resource(User, "/users")
api.add_resource(Message, "/messages")
api.add_resource(Emotion, "/emotion")


