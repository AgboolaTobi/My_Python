def two_sum(numbers, target):
    result = []
    for position in (0, len(numbers)):
        if numbers[position] + numbers[position + 1] == target:
            result.append(position)
    return result


given = [2, 7, 11, 15]
print(two_sum(given, 11))
