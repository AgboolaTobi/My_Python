def my_function():
    number1 = int(input("Enter first number:"))
    number2 = int(input("Enter second number:"))
    result = number1 ** number2
    return result


def square_sum():
    number1 = int(input("Enter first number:"))
    number2 = int(input("Enter second number:"))
    result = number1 ** 2 + number2 ** 2
    return result


print(my_function() + square_sum())
