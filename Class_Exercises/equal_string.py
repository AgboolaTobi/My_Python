def equal_string(numbers1, numbers2):
    same = []
    for i in numbers1:
        for j in numbers2:
            if i == j:
                same.append(i)
            else:
                return False

    return len(numbers1) == len(numbers2) and same


print(equal_string('losve', 'love'))
print(equal_string('love', 'love'))


def equal_strings(first, second):
    validity = True
    for i in first:
        for j in second:
            if i == j and len(first) == len(second):
                return validity
            else:
                return False
    return validity

#
#         if i == j:
#             return validity
#         else:
#             return False
# length = 0
# if len(numbers1) == len(numbers2):
#     length = True
# if length == True and validity:
#     return True
# else:
#     return False
