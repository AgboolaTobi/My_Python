number1 = int(input("Enter first integer: "))
number2 = int(input("Enter second integer: "))
number3 = int(input("Enter third integer: "))

if number1 > number2 and number1 > number3:
        print("Number1 is highest!")

if number2 > number1 > number3:
        print("Number2 ", number2, "is highest!")

if number3 > number2 > number1:
        print("number3", number3, "is highest!")

if number1 < number2 and number1 < number3:
        print("Number1", number1, "is smallest!")

if number2 < number1 and number2 < number3:
        print("Number2", number2, " is smallest!")

if number3 < number2 and number3 < number1:
        print("Number3", number3, "is smallest!")


if number2 < number1 < number3:
        print("Number1", number1, "is the middle number!")

if number1 < number2 < number3:
        print("Number2", number2, " is the middle number!")

if number1 < number3 < number2:
        print("number3", number3, " is the middle number!")


if number1 == number2 or number1 == number3:
        print("Number1 ", number1, " is a duplicate number!")

if number2 == number1 or number2 == number3:
        print("Number2", number2, " is a duplicate number!")

if number3 == number1 or number3 == number2:
        print("Number3", number3, " is a duplicate number")
