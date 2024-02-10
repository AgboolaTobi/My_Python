def the_hcf(numbers):
    result = []
    the_new_array = []
    global new_element
    divisor = 2
    count = 0
    for number in numbers:
        while count != len(numbers) and numbers[count] % divisor == 0:
            count += 1
        if count == len(numbers):
            for index in range(0, len(numbers)):
                numbers[index] /= divisor

        # new_element = number / divisor
        # the_new_array.append(new_element)
        # divisor += 1
        # for element in the_new_array:
        #     if divisor % element == 0:
        #         result.append(element)

    return result


my_numbers = [8, 4, 12]
given = [6, 3, 9]
print(the_hcf(given))
print(the_hcf(my_numbers))
