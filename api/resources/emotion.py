from unittest.main import MAIN_EXAMPLES
import database
from flask_restful import Resource, reqparse
from emoji_weights import EMOJI_WEIGHTS
import math

class Emotion(Resource):
    def get(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str, help="Login is required", required=True)

        args = parser.parse_args()

        user = database.User.query.filter_by(login=args["login"]).first()

        x_user = user.mood_coefficient
        y_user = user.calmness_coefficient


        min_emoji_value = 10000
        result_emoji = ''
        
        for emoji in EMOJI_WEIGHTS:
            current_x = emoji[1]
            current_y = emoji[2]

            current_emoji_value = math.sqrt(math.pow((x_user - current_x), 2)
             + math.pow((y_user - current_y), 2))

            if current_emoji_value < min_emoji_value:
                min_emoji_value = current_emoji_value
                result_emoji = emoji[0]


        return {"result_emoji": result_emoji}