def collect_duplicates(numbers):
    duplicates = []
    for element in numbers:
        if numbers.index(element) == numbers.index(element):
            duplicates.append(element)
    return duplicates


my_list = [1, 2, 3, 3, 2, 4, 5, 6]
my_list2 = [1, 2, 3, 4, 5]
print(collect_duplicates(my_list))
# print(collect_duplicates(my_list2))
