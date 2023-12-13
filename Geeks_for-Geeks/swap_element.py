def swap_element(numbers: list):
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


def change_element_position(numbers: list):
    for i in range(0, len(numbers)):
        for j in range(i - 1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


my_list = [9, 10, 7, 1, 2, 3, 5, 4]
print(my_list)
print(swap_element(my_list))
print(change_element_position(my_list))
