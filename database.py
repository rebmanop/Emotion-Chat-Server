from api import db



class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    login = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    mood_coefficient = db.Column(db.Integer, nullable=True)
    calmness_coefficient = db.Column(db.Integer, nullable=True)

    #def hash_password(self):
    #    self.password = generate_password_hash(self.password).decode('utf8')

    #def check_password(self, password):
    #    return check_password_hash(self.password, password)
   

class Message(db.Model):
    id = db.Column(db.String, primary_key=True)
    content = db.Column(db.String(255))
    receiver_login = db.Column(db.String, nullable=False)
    sender_login = db.Column(db.String, nullable=False)











    

