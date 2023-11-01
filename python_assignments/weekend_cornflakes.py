# list1 = []
#     list2 = []
#     length = len(my_list)
#     if len(my_list) % 2 != 0:
#         return my_list
#     else:
#         for elements in my_list:
#             if length == length / 2:
#                 list1.append(elements)
#             if length > length / 2:
#                 list2.append(elements)
#         return list1, list2
def split_list(my_list):
    half_of_length = len(my_list) // 2
    if len(my_list) % 2 != 0:
        return my_list
    else:
        first = my_list[: half_of_length]
        second = my_list[half_of_length:]
    return f'{first} {second}'


sample_output = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]


# print(split_list(sample_output))


def frequency_of_elements(my_list):
    picked_elements = []
    given_value = int(input("Enter your desired given value of frequency check: "))
    for elements in my_list:
        appearance = my_list.count(elements)
        if appearance > given_value and elements not in picked_elements:
            picked_elements.append(elements)
    return picked_elements


sample_output2 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]


# print(frequency_of_elements(sample_output2))


def difference_of_max_and_min(my_list):
    for elements in my_list:
        return max(my_list) - min(my_list)


def difference_of_max_and_min2(my_list):
    maximum = my_list[0]
    minimum = my_list[-1]
    for element in my_list:
        if element > maximum:
            maximum = element
    for element in my_list:
        if element < minimum:
            minimum = element
    return maximum - minimum


print(difference_of_max_and_min2([10, 75, 20, 30, 15, 5, 40, 25, 40, 35]))


# def two_lists_to_dictionary(my_list1, my_list2):
#     my_dict = {}
#     result = {}
#     for element in my_list1:
#         for elements in my_list2:
#             my_dict.update({element: elements})
#         result.update({element: elements})
#     return result
#
#
# print(two_lists_to_dictionary(['a', 'b', 'c', 'd', 'e'], [1, 2, 3, 4, 5]))


def list_to_dictionary(my_list):
    my_dictionary = {}
    for element in my_list:
        my_dictionary.update({element[0]: element})
    add_new = input("Enter a key: ").lower()
    for element in my_list:
        if add_new not in my_list:
            my_dictionary.update({add_new[0].capitalize(): add_new})
    return my_dictionary


sample_input = ['apple', 'banana', 'coconut']
print(list_to_dictionary(sample_input))
print(list_to_dictionary(sample_input).update({'c': 'corn'}))
