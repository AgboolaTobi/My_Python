def change_occurrence(words: str):
    first_letter = words[0]
    result = words.replace(first_letter, "$")
    return first_letter + result[1:]


# print(change_occurrence('restart'))

# def change_occurrence(letters, index):
#     result = " "
#     for letter in letters:
#         if letters[0] == letters[index]:
#             letter[index] = '$'
#         result.replace(range(letters[0], len(letters)))
#     return result
# print(change_occurrence('restart'))
print(5 // 2)