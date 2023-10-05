my_array = ['A', 'M', 'C', 'W', 'I', 'T']
n = len(my_array) / 2


def shuffle(my_array, result):
    return [my_array[element:: result] for element in range(result)]


print(shuffle(my_array, n))
