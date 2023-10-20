def check_and_count_int(numbers: list):
    store = []
    for _ in numbers:
        for elements in numbers:
            if elements == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
                store.append(elements)

    return len(store)


my_list2 = ["235fht", "fer567AWE", "6-879and"]
my_list = ["ABc21f", "130cpz", "A61L"]
print(check_and_count_int(my_list))
# print(check_and_count_int(my_list2))
