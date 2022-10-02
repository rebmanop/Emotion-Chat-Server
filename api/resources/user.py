import uuid
import database
from api import db  
from flask import request
from flask_restful import Resource, reqparse

class User(Resource):

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str, help="Login is required", required=True)
        parser.add_argument("password", type=str, help="Master password hash is required", required=True)

        args = parser.parse_args()

        user = database.User.query.filter_by(login=args["login"]).first()

        if user and args["password"] != user.password:
            return {"status": 401}
        elif user and args["password"] == user.password:
            return {"status": 200}

        new_user = database.User(id=str(uuid.uuid4()), login=args["login"], password=args["password"], 
        mood_coefficient=50, calmness_coefficient=50)
        
        db.session.add(new_user)
        db.session.commit()

        return {"status": 201}


    def get(self):
        args = request.args
        requested_login = args.get("requested_login")

        user = database.User.query.filter_by(login=requested_login).first()

        if user:
            return {"status": 200}

        return {"status": 404}







        
















