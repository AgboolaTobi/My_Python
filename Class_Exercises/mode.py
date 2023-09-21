number = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20]
print("Original List:", number)

for i in range(0, len(number)):
    for j in range(i+1, len(number)):
        if number[i] >= number[j]:
            number[i], number[j] = number[j], number[i]

# print("arranged list:", number)

different_numbers = []
mode_numbers = []
for i in number:
    if i in different_numbers:
        different_numbers.append(i)
    else:
        mode_numbers.append(i)
print(mode_numbers)