first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))
third_number = int(input("Enter third number:"))
sum = first_number + second_number + third_number
average = sum / 3
product = first_number * second_number * third_number

print("The sum of", first_number, ",", second_number, "and", third_number, "=", sum)
print("The average of", first_number, ",", second_number, "and", third_number, "=", average)
print("The product of", first_number, ",", second_number, "and", third_number, "=", product)

if first_number > second_number and first_number > third_number:
    print("Number1 is highest!")

if second_number > first_number and second_number > third_number:
    print("Number2 is highest!")

if third_number > second_number and third_number > first_number:
    print("number3 is highest!")

if first_number < second_number and first_number < third_number:
    print("Number1 is smallest!")

if second_number < first_number and second_number < third_number:
    print("Number2 is smallest!")

if second_number > first_number > third_number:
    print("number3 is smallest!")
