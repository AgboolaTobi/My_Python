# def fibonacci(number: int) -> int:
#     x = 0
#     y = 1
#     total = x + y
#     while x < number:
#         print(x, end=' ')
#         x = y
#         y = total
#         total = x + y
#     return total
#
# fibonacci(9)


# 2

# def number(number1):
#     if number1 > 0:
#         square = number1 * number1
#         return square
#     if number1 < 0:
#         square = 1 / (number1 * number1)
#     return square
#
#
# print(number())

# 3

def my_square(number: int):
    if number < 0:
        return "Number cannnot be less than 0"
    else:
        return number ** 2


print(my_square(-1))

gallons = float(input("Enter the gallons used(-1 to end):"))
miles = float(input("Enter miles driven:"))
miles_per_gallons_used = miles / gallons
counter = 0
total = 0
while True:
    total = total + miles_per_gallons_used
    print("The miles/gallons=", miles_per_gallons_used)

    gallons = float(input("Enter the gallons used(-1 to end):"))
    if gallons == -1:
        break
    miles = float(input("Enter miles driven:"))
    miles_per_gallons_used = miles / gallons


print(total)
gallons += 1

