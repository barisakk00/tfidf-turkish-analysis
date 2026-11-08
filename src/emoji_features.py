from emoji import emoji_list


def extract_emoji_tokens(text):
    return [item["emoji"] for item in emoji_list(str(text))]
