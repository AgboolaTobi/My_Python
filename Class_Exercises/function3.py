name = 'tosin'
lists = [1, 2, 3, 4, 5]


# keyword argument
def tosin(number, name):
    for n in range(number):
        print(name)


tosin(name="sleeping", number=5)

name = 'tosin'
lists = [1, 2, 3, 4, 5]


#  positional argument
def tosin(number, name):
    return name * number


print(tosin(number=5, name="joy "))


# default arguments
def tosin(name, number=3):
    return name * number


#
# print(tosin(name="Joy ", number=10))

#
# name = 'tosin'
# number = [1, 2, 3, 4, 5]
#
# type annotation(This is not really needed,it's just used for code readability)
# Example1
# def tosin(name: str, number: int) -> str:
#     for x in range(number):
#         print(name)
# print(tosin("toby", number))
# Example2
def me(name: str, number: int, age: str) -> str:
    Employees_details = name, number, age


me("toby", 60, 21)
print(me("toby", 60, 21))
