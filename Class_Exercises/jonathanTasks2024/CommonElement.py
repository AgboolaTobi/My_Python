def common(array1, array2):
    global picked
    result = []
    for element in array1:
        for those in array2:
            if element == those:
                result.append(element)
    minimum = result[0]
    for picked in result:
        if picked > minimum:
            picked = minimum

    return picked


first = [2, 3, 5, 6, 7, 8]
second = [1, 3, 7, 10, 11, 8]


third = [5, 4, 11, 13, 9]
fourth = [9, 11, 15, 1, 14]

print(common(first, second))

print(common(third, fourth))
