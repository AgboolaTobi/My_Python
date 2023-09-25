number = int(input("Enter a five digit integer: "))
for number in range(number):
    number1 = int(number / 10000)
    number2 = int(number/1000) % 10
    number3 = int(number/100) % 10
    number4 = int(number / 10) % 10
    number5 = number % 10

print("\t", "\t", "\t", "\t", "\t", number1, number2, number3, number4, number5)
