from api import db

class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    login = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    mood_coefficient = db.Column(db.Integer, nullable=True)
    calmness_coefficient = db.Column(db.Integer, nullable=True)
    

class Message(db.Model):
    id = db.Column(db.String, primary_key=True)
    content = db.Column(db.String(255))
    receiver_login = db.Column(db.String, nullable=False)
    sender_login = db.Column(db.String, nullable=False)
    time = db.Column(db.Float, nullable=False )













    

