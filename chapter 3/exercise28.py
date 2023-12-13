values = [9, 11, 22, 34, 17, 22, 34, 22, 40]


def mean(numbers: list):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


def sorting_numbers(numbers: list):
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] <= numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


def median(numbers: list):
    if len(numbers) % 2 == 0:
        median_of_numbers = numbers[len(numbers) // 2]
    else:
        mid1 = len(numbers) // 2
        mid2 = mid1 - 1
        median_of_numbers = (numbers[mid1] + numbers[mid2]) / 2
    return median_of_numbers


print(mean(values))
print(sorting_numbers(values))
print(median(sorting_numbers(values)))
