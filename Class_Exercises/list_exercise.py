def add_function(numbers: list):
    result = 0
    for element in numbers:
        result = result + element
    return result


def multiply_function(numbers: list):
    product = 1
    for element in numbers:
        product *= element
    return product


def find_largest_number(numbers: list):
    largest_number = numbers[0]
    for number in numbers:
        if number > largest_number:
            largest_number = number
    return largest_number


def find_smallest_number(numbers: list):
    smallest_number = numbers[0]
    for number in numbers:
        if number < smallest_number:
            smallest_number = number
    return smallest_number


def no_duplicate_number(numbers: list):
    different_numbers = []
    for number in range(len(numbers)):
        if numbers[number] not in different_numbers:
            different_numbers.append(numbers[number])
    return different_numbers
