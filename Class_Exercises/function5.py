# def my_sum(*numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     return total
#
#
# print(my_sum(2, 3, 5,  6, 12, 13, 14, 15))


# The below is an example of the inbuilt sum which adds a list of numbers
# print(sum([2, 3, 5, 6, 12, 13, 14, 15]))


def addition_of_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def multiplication(*numbers):
    product = 1
    for number in numbers:
        product += number
    return product


print(multiplication(4, 5))

print(addition_of_numbers(1, 2, 3, 4, 5))
