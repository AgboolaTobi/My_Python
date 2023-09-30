number = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20]
sum = 0
length = len(number)
print("The length of characters in number=", length)
for number in number:
    sum = sum + number

print("The sum:", sum)

mean = sum / length
print("The mean=", mean)
