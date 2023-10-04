numbers = [15, 20, 25, 20, 10, 5]
for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] >= numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Numbers arranged in ascending order:", numbers)
smallest = numbers[0]
print(smallest)
