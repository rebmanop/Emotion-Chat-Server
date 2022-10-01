import uuid
import database
from flask_restful import Resource, reqparse
from emoji_weights import EMOJI_WEIGHTS, get_content_weight
from api import db

class Message(Resource):
    
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument("content", type=str, help="Message content is required", required=True)
        parser.add_argument("sender_login", type=str, help="Sender id is required", required=True)
        parser.add_argument("receiver_login", type=str, help="Receiver id is required", required=True)

        args = parser.parse_args()

        new_message = database.Message(id=str(uuid.uuid4()),content=args["content"], sender_login=args["sender_login"], receiver_login=args["receiver_login"])
        db.session.add(new_message)
        db.session.commit()

        sender_messages = database.Message.query.filter_by(sender_login=args['sender_login']).all()
        receiver_messages = database.Message.query.filter_by(receiver_login=args['receiver_login']).all()
        print(len(sender_messages), len(receiver_messages))
        
        sum_mk = 0
        sum_ck = 0
        for message in receiver_messages:
            content = message.content
            mk, ck = get_content_weight(content)
            sum_mk += mk
            sum_ck += ck

        receiver_user = database.User.query.filter_by(login=args['receiver_login']).first()
        sum_mk = sum_mk / 2 + 50
        sum_ck = sum_ck / 2 + 50
        receiver_user.mood_coefficient =  sum_mk / (len(receiver_messages) + 1)
        receiver_user.calmness_coefficient = sum_ck / (len(receiver_messages) + 1)

        sum_mk = 0
        sum_ck = 0
        for message in sender_messages:
            content = message.content
            mk, ck = get_content_weight(content)
            sum_mk += mk
            sum_ck += ck

        sender_user = database.User.query.filter_by(login=args['sender_login']).first()
        sum_mk = sum_mk + 50
        sum_ck = sum_ck + 50
        
        sender_user.mood_coefficient = sum_mk / (len(sender_messages) + 1)
        sender_user.calmness_coefficient = sum_ck /  (len(sender_messages) + 1)

        db.session.commit()

        return 200





    


    

    



    
    









    