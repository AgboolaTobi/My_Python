def number():
    number1 = int(input("Enter number1:"))
    number2 = int(input("Enter number2:"))
    result = number1 * number2
    if number1 % number2 == 0:
        return result
    if number1 % number2 == 1:
        return result
    if number1 == 9 and number2 == 2:
        return


print(number())
