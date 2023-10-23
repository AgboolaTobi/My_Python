def sort_dictionary(dictionary):
    sorted_dictionary = {}
    for key, value in dictionary.items():
        sorted_dictionary = sorted(dictionary.items())
    return dict(sorted_dictionary)


def reverse_dictionary(dictionary):
    result = {}
    result = dict(reversed(sorted(dictionary.items())))
    return result


def add_key(my_dictionary, key, value):
    # my_dictionary[key] = value
    my_dictionary.update({key: value})
    return my_dictionary


my_dictionary = {1: 10, 2: 20}
print(add_key(my_dictionary, 3, 30))
my_dictionary.update({3: 30})
print(my_dictionary)

sample = {2: 4, 1: 1, 3: 9, 5: 25, 4: 16}
print(sort_dictionary(sample))
print(reverse_dictionary(sample))
