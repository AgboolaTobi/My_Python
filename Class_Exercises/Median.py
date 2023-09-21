number = [1, 2, 3, 4, 5, 5, 6, 7, 1, 3, 5, 6]
print("Original list:", number)
length = len(number)

print("The length of 'number' =",length)

for i in range(0, length):
    for j in range(i+1, length):
        if number[i] >= number[j]:
            number[i], number[j] = number[j], number[i]

print("arranged list:", number)

if length % 2 == 0:
    mid1 = length // 2
    mid2 = mid1 - 1
    median = (number[mid1] + number[mid2]) / 2
else:
    mid = length // 2
    median = number[mid]
print("The median = ", median)

