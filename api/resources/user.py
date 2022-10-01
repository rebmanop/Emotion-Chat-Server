import database
from flask_restful import Resource, reqparse
from api import db  
import uuid


class User(Resource):

    def post(self):
        """Sign up procedure"""

        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str, help="Login is required", required=True)
        parser.add_argument("password", type=str, help="Master password hash is required", required=True)
       

        args = parser.parse_args()

        new_user = database.User(id=str(uuid.uuid4()), login=args["login"], password=args["password"], mood_coefficient=50, calmness_coefficient=50)
        
        db.session.add(new_user)
        db.session.commit()

        return 201 

    def get(self):
        pass












