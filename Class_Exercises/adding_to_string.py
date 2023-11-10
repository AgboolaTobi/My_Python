def add_sting_to_string(word: str):

    if len(word) < 3:
        return word
    elif len(word) >= 3 and not word.endswith("ing"):
        return word + "ing"
    else:
        if len(word) > 3 and word.endswith("ing"):
            return word + "ly"


print(add_sting_to_string("str"))
