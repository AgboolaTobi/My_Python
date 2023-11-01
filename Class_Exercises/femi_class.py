def collect_duplicates(numbers):
    duplicates = []
    for element in numbers:
        if numbers[element] == numbers[element]:
            duplicates.append(element)
    return duplicates


my_list = [1, 2, 3, 3, 2, 4, 5, 6]
print(collect_duplicates(my_list))
