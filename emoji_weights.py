
EMOJI_WEIGHTS = [
                ["U+1F600", 0, 0], #😢
                ["U+1F611", 50, 0], #😑
                ["U+1F60C", 100, 0], #😌
                ["U+2639", 0, 50], #☹
                ["U+1F610", 50, 50], #😐
                ["U+1F642", 100, 50], #🙂
                ["U+1F620", 0, 100], #😠
                ["U+1F603", 50, 100], #😃
                ["U+1F601", 100, 100] #😁
                ]


def get_content_weight(content):
    for emoji in EMOJI_WEIGHTS:
        if emoji[0] == content:
            return emoji[1], emoji[2]
            