my_playlist = []
names = ["arua", "joy", "qudus", "ope"]
names2 = list("isreal")
tuple1 = 1, 2, 3
tuple2 = 'a', 'b', 'c'

list_to_tuple = tuple(names)
print(list_to_tuple)

tuple_to_list = list(list_to_tuple)
print(tuple_to_list)

print(names + names2)

# the below will not work because they're not of the same type
# tuple1 += names
# print(tuple1)

# this below explains homogeneity of list
names[0] = "tosin"
print(names)

tuple3 = (1, 2, 3, "ope", ["precious", "joy"], "delighted")
tuple3[4][0] = "mercy"
print(tuple3)

lt = list(tuple3)
lt[3] = "tobi"
tuple3 = tuple(lt)
print(tuple3)

ans = tuple3[1] * 5
print(ans)

a = (1, (2, 3), ("a", "b"), 4, [5, 6], True)
b = ["ope", "arua", "joy", (1, 2), [3, 4], ]
# unpackaging a tuple
tuple5 = 1, 2, 3
x = tuple5[0]
y = tuple5[1]
z = tuple5[2]

print(x, y, z)

tuple6 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
a = tuple6[1]
b = tuple6[5]
b, a, *others = tuple6
print(others, a, b)

# slicing a tuple
tuple6 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(tuple6[2:7:1])

names = ["arua", "joy", "qudus", "ope"]
a, b, *c = names
print(a, b, c)

# slicing method can be used to delete items from a tuple

del names[1]
print(names)
# the del can also be used to delete the entire elements in a list by doing del name[:],this will leave an empty list
# names


print(names.pop())
# pop takes the index of an item in a list and removes it. if any index is not passed,the last item is removed
#  the .remove take off a specified item from a list. note that this does not take index but the element in the position

# you can also use the count method in a list and in a tuple. It will count the number of times an item appears

# the following evaluate to falsy
# 0,''(an empty string), false,[],(),0.0,
# the following evaluate as trueity values
# 'ope',True,[1,'o'], (1,),{}(is any dictionary with something inside it),0.1,1.1

# the all method is a built in function that iterates over a colection and returns true if the collections are
# trueity or falsey. it takes iterables(a list or tuple)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(all(numbers))

# the function 'any' checks whether a value is a falsey value or truity value. the any function only checks for
# anyone of the collection that is either true or false

print(any(numbers))


