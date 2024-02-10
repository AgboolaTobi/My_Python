def thursday(array):

    for length in array:
        for element in length:
            array[element] = array[length]
    return array


check = [[2, 3], [4, 5]]

print(thursday(check))
