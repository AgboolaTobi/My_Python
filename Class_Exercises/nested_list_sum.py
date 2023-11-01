def sum_list(numbers):
    sum_of_elements = 0
    for index in numbers:
        for elements in index:
            sum_of_elements += elements

    return sum_of_elements


print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))


def sum_list2(numbers):
    sum_elements = 0
    for elements in numbers:
        sum_elements += sum(elements)
    return sum_elements


# print(sum_list2([[2, 4, 5, 6], [2, 3, 5, 6], [3, 4]]))


def sum_list3(numbers):
    a, b = numbers
    result = sum(a) + sum(b)
    return result


# You can also use the star arges for arbitrary numbers

# print(sum_list3([[2, 4, 5, 6], [2, 3, 5, 6]]))

