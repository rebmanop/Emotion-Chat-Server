import uuid
import time
import database
from api import db
from operator import attrgetter
from flask_restful import fields, marshal, marshal_with
from emoji_weights import EMOJI_WEIGHTS, get_content_weight
from flask_restful import Resource, reqparse, request


resource_fields = {
                  'sender_login': fields.String, 
                  'receiver_login': fields.String,
                  'content': fields.String
                  }

class Message(Resource):
    
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument("content", type=str, help="Message content is required", required=True)
        parser.add_argument("sender_login", type=str, help="Sender id is required", required=True)
        parser.add_argument("receiver_login", type=str, help="Receiver id is required", required=True)

        args = parser.parse_args()

        new_message = database.Message(id=str(uuid.uuid4()),content=args["content"], 
        sender_login=args["sender_login"], receiver_login=args["receiver_login"], time=time.time())
        db.session.add(new_message)
        db.session.commit()

        sender_messages = database.Message.query.filter_by(sender_login=args['sender_login']).all()
        receiver_messages = database.Message.query.filter_by(receiver_login=args['receiver_login']).all()
        
        sum_mk, sum_ck = self.get_koefs_sum(sender_messages)

        sender_user = database.User.query.filter_by(login=args['sender_login']).first()
        sum_mk = sum_mk + 50
        sum_ck = sum_ck + 50
        sender_user.mood_coefficient = sum_mk / (len(sender_messages) + 1)
        sender_user.calmness_coefficient = sum_ck /  (len(sender_messages) + 1)


        sum_mk, sum_ck = self.get_koefs_sum(receiver_messages)

        receiver_user = database.User.query.filter_by(login=args['receiver_login']).first()
        sum_mk = sum_mk / 2 + 50
        sum_ck = sum_ck / 2 + 50
        receiver_user.mood_coefficient =  sum_mk / (len(receiver_messages) + 1)
        receiver_user.calmness_coefficient = sum_ck / (len(receiver_messages) + 1)



        db.session.commit()

        return {"status": 200}


    def get_koefs_sum(self, messages):
        sum_mk = 0
        sum_ck = 0
        for message in messages:
            content = message.content
            mk, ck = get_content_weight(content)
            sum_mk += mk
            sum_ck += ck

        return sum_mk, sum_ck

    
    @marshal_with(resource_fields)
    def get(self):

        args = request.args
        
        messages = database.Message.query.filter_by(sender_login=args.get("current_user_login"), receiver_login=args.get("other_user_login")).all()
        messages += database.Message.query.filter_by(sender_login=args.get("other_user_login"), receiver_login=args.get("current_user_login")).all()
        
        messages.sort(key=attrgetter('time'))

        return messages









    


    

    



    
    









    