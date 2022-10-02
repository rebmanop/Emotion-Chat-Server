
# EMOJI_WEIGHTS = [
#                 ["U+1F600", 0, 0],
#                 ["U+1F611", 50, 0], 
#                 ["U+1F60C", 100, 0], 
#                 ["U+2639", 0, 50], 
#                 ["U+1F610", 50, 50],
#                 ["U+1F642", 100, 50], 
#                 ["U+1F620", 0, 100], 
#                 ["U+1F603", 50, 100], 
#                 ["U+1F601", 100, 100] 
#                 ]


EMOJI_WEIGHTS = [
                ["\uD83D\uDE22", 0, 0], 
                ["\uD83D\uDE11", 50, 0], 
                ["\uD83D\uDE0C", 100, 0],  
                ["\uD83D\uDE41", 0, 50], 
                ["\uD83D\uDE10", 50, 50],
                ["\uD83D\uDE42", 100, 50], 
                ["\uD83D\uDE20", 0, 100], 
                ["\uD83D\uDE03", 50, 100], 
                ["\uD83D\uDE01", 100, 100] 
                ]
                

def get_content_weight(content):
    for emoji in EMOJI_WEIGHTS:
        if emoji[0] == str(content):
            return emoji[1], emoji[2]
        else:
            return EMOJI_WEIGHTS[4][1], EMOJI_WEIGHTS[4][2]

           
    
                