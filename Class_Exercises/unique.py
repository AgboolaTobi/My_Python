def unique(numbers):
    unique_elements = []
    for elements in set(numbers):
        if elements % 2 == 0:
            unique_elements.append(elements)
    return unique_elements


print(unique([1, 3, 2, 5, 3, 4, 6, 4, 6, 9, 8, 2, 10, 8, 12, 15, 10, 6, 14]))

dav = [1, 2, 3, 6, 4, 5, 6, 7, 8, 9]

print(unique(dav))


def unique2(numbers):

    return list(i for i in numbers if i % 2 == 0)


print(unique2([1, 3, 2, 5, 3, 4, 6, 4, 6, 9, 8, 2, 10, 8, 12, 15, 10, 6, 14]))
