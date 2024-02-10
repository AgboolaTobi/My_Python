def duplicates(given):
    for i in range(0, len(given)):
        for j in range(i + 1, len(given)):
            if given[i] >= given[j]:
                given[i], given[j] = given[j], given[i]
    return given


print(duplicates([1, 4, 5, 3, 6]))

# different_numbers = []
# mode_numbers = []
# for i in given:
#     if i not in different_numbers:
#         different_numbers.append(i)
#         print(different_numbers)
#     else:
#         mode_numbers.append(i)
# return mode_numbers
