import random
from string import ascii_letters,ascii_lowercase,hexdigits


def mylist():
    team_four = []
    for element in range(1, 21):
        team_four.append(element)
    return team_four


def odd_list():
    odd = []
    for element in mylist():
        if element % 2 != 0:
            odd.append(element)
    return odd


def double():
    double_element = []
    for element in odd_list():
        double_element.append(element * 2)
    return double_element


def odd_check(number):
    return number % 2 == 1


# the filter function is a higher order function that takes in another function as its parameter. When using the
# filter function, you only need to write the called function's name as only a reference not the function
def mr_sikiru1(list1):
    return list(filter(odd_check, list1))


# the lambda for
def mr_sikiru2(list2):
    return list(filter(lambda x: x % 2 == 1, list2))


def mr_sikiru3(list3):
    return [i * 2 for i in list3 if i % 2 == 1]


def change_element(list4):
    result = [i * 2 for i in list4 if i % 2 == 1]
    result[4:8] = [0] * len(list4[4:8])
    return result


def concatenate(list5, list6):
    return [x + y for x, y in zip(list5, list6)]


# The map function works like the filter function. It does the operation the algorithm instructs the same way.
# Knowing when to use them is important. A filter is used when you want your algorithm to filter a list and return
# based on the algorithm. The map is used when your algorithm will not be filtering or removing from the list
# NOTE THAT THE MAP ONLY VALIDATES TRUE OR FALSE AND PRINTS TRUE OR FALSE BASED ON THE ALGORITHM

numbers = list(range(1, 21))


def even(n):
    return n % 2 == 0


print(list(filter(lambda x: x % 2 == 0, numbers)))
print(list(map(even, numbers)))
result = list(filter(lambda x: x % 2 == 1 and x % 3 == 0, numbers))

# zip is an inbuilt function that maps elements in the same indexes from two or more list and pairs them in a list
number2 = list(range(1, 13))
number3 = list(range(1, 13))
number4 = list(range(1, 10))
print(list(zip(number2, number3, number4)))

print(random.choice([1, 2, 3, 4, 5]))
leters = list(ascii_letters)
digits = list(hexdigits)

print(leters)
print(digits)
random.shuffle

