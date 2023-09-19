#
# sum = 0
# for count in range(2, 51, 2):
#     print(count, end=" ")
# result = count
# number = len(result)
# print(number)

# sum = 0
# count = 0
# even = 0
# while even < 50:
#     even += 2
#     count += 1
#     sum = sum + even
# average = sum / count
# print(f'{average:.2f}')


even_numbers = []
for count in range(2, 51, 2):
    even_numbers.append(count)
print(even_numbers)
average = sum(even_numbers) / len(even_numbers)
print(average)
