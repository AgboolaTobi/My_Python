numbers = [15, 20, 25, 20, 10, 5]
result_of_multiple = []
for element in numbers:
    result_of_multiple.append(element*2)
print(result_of_multiple)

# because of the mutability nature of list, you dont need another list to add your result

numbers = [15, 20, 25, 20, 10, 5]
for i in numbers:
    numbers = i*2
    print(numbers, end=" ")

# Done sir
