# string = 'google.com'
#
# for element in string:
#     string.count(element)
#     print(string.count(element), end=" ")
# splitted = []
# for element in string:
#     string.split(element)
#     splitted.append(element)
# print(splitted)
#
# dict = {}
# for key, value in dict.items():
#     if key == string:
#         value == splitted
#     dict.update({key: value})
#
#
# def frequency_character(string):
#     global elements, element
#     dict = {}
#     for elements in string:
#         string.count(elements)
#     for element in string:
#         string.split(element)
#         splitted.append(element)
#     for key, value in dict.keys():
#         key = string.count(elements)
#         value = string.split(element)
#         dict.update({key: value})
#     return dict
#
#
# print(frequency_character(string))


def frequency(string):
    dict = {}
    for element in string:
        dict.update({element: string.count(element)})
    return dict


string = 'google.com'
print(frequency(string))


def character_frequency_correction(words: str):
    result = {}
    for character in words:
        if character in result.keys():
            result[character] += 1
        else:
            result[character] = 1
    return result


def character_frequency_correction2(words: str):
    return {word: words.count(word) for word in words}
