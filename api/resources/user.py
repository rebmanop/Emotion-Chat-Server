from email.policy import default
import database
from flask_restful import Resource, reqparse
from flask import request
from api import db  
import uuid


class User(Resource):

    def post(self):
        """Sign up procedure"""

        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str, help="Login is required", required=True)
        parser.add_argument("password", type=str, help="Master password hash is required", required=True)

        args = parser.parse_args()

        user = database.User.query.filter_by(login=args["login"]).first()

        if user and args["password"] != user.password:
            return {"status": 401}
        elif user and args["password"] == user.password:
            return {"status": 200}

        new_user = database.User(id=str(uuid.uuid4()), login=args["login"], password=args["password"], mood_coefficient=50, calmness_coefficient=50)
        
        db.session.add(new_user)
        db.session.commit()

        return {"status": 201}


    def get(self):
        args = request.args
        login = args.get("login")
        other_login = args.get("other_login")


        user = database.User.query.filter_by(login=other_login).first()

        if user:
            #default_message = database.Message(id=str(uuid.uuid4()), 
            #content="U+1F610", receiver_login=other_login, sender_login=login)

            #db.session.add(default_message)
            #db.session.commit()
            return {"status": 200}

        return {"status": 404}







        
















