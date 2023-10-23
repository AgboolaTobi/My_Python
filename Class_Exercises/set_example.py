# my_set = {1, 2, 3, 3, 4, 5, 2, 1}
# my_set = list(my_set)
# print(my_set)
# my_set1 = set()
# # my_set.update("234")
# print(my_set1)
# my_set.remove(5)
# print(my_set)
# for numbers in range(6):
#     my_set1.add(numbers)
# print(my_set1)
# print(my_set)
#
# numbers = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20]
# my_set2 = set(numbers)
# print(my_set2)
# # Note that thought a set is mutable, the items in the set must be immutable. It means I can remove and add to a set
# # but the items in the set must be immutable. You cannot put a list or set in a set !
#
# # Set contain list of unordered set of unique elements. It means at every run time the elements can change positions.
# # Therefore, there is no indexing in sets
# numbers = my_set2
# print(list(numbers))
# numbers = set(numbers)
# print(list(numbers))

my_set4 = {1, 1.1, "ope", 1, 2, "ope", (1, 2, 1)}
print(my_set4)
print(len(my_set4))
my_set4.update("tobi")
print(my_set4)
my_set5 = frozenset({1, 3, 5, 7, 9})
frozenset(my_set4)
my_set4.union({1, 2, 3, 4, 5, 5})
print(my_set4)
print(2 in my_set4)
