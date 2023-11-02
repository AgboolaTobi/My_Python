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


# print(difference_of_max_and_min2([10, 75, 20, 30, 15, 5, 40, 25, 40, 35]))


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


def list_to_dictionary(my_list, checker):
    my_dictionary = {}
    for elements in my_list:
        my_dictionary.update({elements[0]: elements})
        my_dictionary.update({checker[0]: checker})
    if checker in my_list:
        my_dictionary.update({checker[0].capitalize(): checker})
    return my_dictionary


sample_input = ['apple', 'banana', 'coconut']
print(list_to_dictionary(sample_input, 'crab'))


def list_to_dictionary2(my_list):
    dict = {}
    for entry in my_list:
        dict.update({entry[0]: entry})
    return dict


# print(list_to_dictionary(sample_input))
# print(list_to_dictionary2(sample_input))


def two_list_to_dictionary(my_list1, my_list2):
    if len(my_list1) != len(my_list2):
        return f'{my_list1}'
    else:
        return dict(zip(my_list1, my_list2))


input1 = ['a', 'b', 'c', 'd', 'e']
input2 = [1, 2, 3, 4, 5]


# print(two_list_to_dictionary(input1, input2))


def remove_multiple_empty_strings(my_list):
    return [element for element in my_list if len(element) > 0]


sample_list = ['', 'ABC', 'xyz', '', 'abc', 'XYZ']
print(remove_multiple_empty_strings(sample_list))


def list_to_dictionary5(my_list, checker):
    my_dictionary = {}
    if checker in my_list:
        for elements in my_list:
            return my_dictionary.update({elements[0]: elements})
    else:
        my_dictionary.update({checker[0].capitalize(): checker})
        return my_dictionary


def list_to_dictionary_correction(my_list):
    dictionary = {}
    for count in my_list:
        result = count[0]
        if result in dictionary:
            result = count[0].upper()
        dictionary[result] = count
    return dictionary


sample_input = ['apple', 'banana', 'coconut']


# print(list_to_dictionary_correction(sample_input))


def two_lists_to_dictionary_correction(list1, list2):
    return {value1: value2 for (value1, value2) in enumerate(zip(list1, list2))}
