def character_frequency(words: str):

    result = {}

    for character in words:
        if character in result.keys():
            result[character] += 1
        else:
            result[character] = 1
    return result


question = "semicolon"

print(character_frequency(question))
