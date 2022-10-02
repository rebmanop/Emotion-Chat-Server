
from flask_restful import Resource, request
import database

class Chat(Resource):
    def get(self):
            args = request.args
            login = args.get("login")

            chats_with_users = set()
            message_list = database.Message.query.filter_by(sender_login=login).all()
            message_list += database.Message.query.filter_by(receiver_login=login).all()

            for message in message_list:
                chats_with_users.add(message.sender_login)
                chats_with_users.add(message.receiver_login)

            if login in chats_with_users:
                chats_with_users.remove(login)

            chats_with_users = list(chats_with_users)

            if len(chats_with_users) == 0:
                return {"status": 404}

            return {"chats": chats_with_users}