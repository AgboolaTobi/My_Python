number = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", number)

for i in range(0, len(number)):
    for j in range(i+1, len(number)):
        if number[i] >= number[j]:
            number[i], number[j] = number[j], number[i]

print("arranged list:", number)

if len(number) % 2 == 0:
    mid1 = len(number) // 2
    mid2 = mid1 - 1
    median = (number[mid1] + number[mid2]) / 2
else:
    mid = len(number) // 2
    median = number[mid]
print(median)


# nice job pls stop naming my file like java file, this should be median.py 
# median.py file may already exist in python so you look for another suitable name sir
