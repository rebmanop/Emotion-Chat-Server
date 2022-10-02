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
            print("user exist incorrect")
            return {"status": 401}
        elif user and args["password"] == user.password:
            print("user exist correct")
            return {"status": 200}

        new_user = database.User(id=str(uuid.uuid4()), login=args["login"], password=args["password"], mood_coefficient=50, calmness_coefficient=50)
        print("created_new")
        db.session.add(new_user)
        db.session.commit()

        return {"status": 201}


    def get(self):
        """get chats for the user"""

        args = request.args
        login = args.get("login")

        chats_with_users = set()
        message_list = database.Message.query.filter_by(sender_login=login).all()
        message_list += database.Message.query.filter_by(receiver_login=login).all()

        for message in message_list:
            chats_with_users.add(message.sender_login)
            chats_with_users.add(message.receiver_login)


        chats_with_users.remove(login)
        chats_with_users = list(chats_with_users)

        return {"chats": chats_with_users}



        
















