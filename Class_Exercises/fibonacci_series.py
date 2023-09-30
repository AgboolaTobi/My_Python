# while loop done with count
print('\nwhile loop done with count ')
number1 = 0
number2 = 1
count = 0
while number1 < 50:
    print(number1, end=' ')
    total = number1 + number2
    number1 = number2
    number2 = total
    count += 1

# for loop
print("\nfor loop done without count ", total)

number1 = 0
number2 = 1
total = number1 + number2
for i in range(0, 51):
    if number1 > 50:
        break
    print(number1, end=' ')
    number1 = number2
    number2 = total
    total = number1 + number2

print("\nwhile loop done without count ", total)
# while loop done without count
number1 = 0
number2 = 1
total = number1 + number2
while number1 < 50:
    print(number1, end=' ')
    number1 = number2
    number2 = total
    total = number1 + number2
