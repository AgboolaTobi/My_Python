# an example of list comprehension
def my_sort_funct(my_list1: list):
    for i in range(0, len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] >= my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]

    return my_list


my_list = [8, 10, 12, 2, 18, 20, 4, 6, 14, 16]
print(my_sort_funct(my_list))


