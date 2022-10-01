EMOJI_WEIGHTS = {
    "U+1F600": (80, 40), # smiley face
    "U+2639": (30, 10)
}

def get_content_weight(content):
    koefs = EMOJI_WEIGHTS.get(content)
    return koefs[0], koefs[1]