number1 = int(input("Enter first integer: "))
number2 = int(input("Enter second integer: "))
number3 = int(input("Enter third integer: "))

sum = number1 + number2 + number3
print("Some of",number1,",",number2,",",number3, "=",sum)

average = sum/3
print("The average of",number1,",",number2,",",number3,"=",round(average, 3))

product = number1 * number2 * number3
print("The product of",number1,",",number2,",",number3,"=",product)

if number1 > number2 and number1 > number3:
        print("Number1 is highest!")

if number2 > number1 and number2 > number3:
        print("Number2 is highest!")

if number3 > number2 and number3 > number1:
        print("number3 is highest!")

if number1 < number2 and number1 < number3:
        print("Number1 is smallest!")

if number2 < number1 and number2 < number3:
        print("Number2 is smallest!")

if number3 < number2 and number3 < number1:
        print("number3 is smallest!")
