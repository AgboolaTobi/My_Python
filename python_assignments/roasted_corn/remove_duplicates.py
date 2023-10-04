numbers = [15, 20, 25, 20, 10, 5]
for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] >= numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
different_numbers = []

mode_numbers = []

for i in numbers:
    if i in different_numbers:
        different_numbers.append(i)

    else:
        mode_numbers.append(i)
print(mode_numbers)
print(different_numbers)

