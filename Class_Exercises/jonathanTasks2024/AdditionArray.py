def addTheElements(numbers):
    global first, second
    result = []
    counter = 1
    if len(numbers) % 2 == 0:
        for element in range(0, len(numbers), 2):
            first = numbers[element]
            second = numbers[counter]
            counter += 2
            result.append(first + second)
        return result
    else:
        for element in range(0, len(numbers)-1, 2):
            first = numbers[element]
            second = numbers[counter]
            counter += 2
            result.append(first+second)
        result.append(numbers[len(numbers)-1])
        return result


given = [2, 3, 5, 6, 7, 2]
print(addTheElements(given))

given = [3, 4, 5, 1, 5]
print(addTheElements(given))
