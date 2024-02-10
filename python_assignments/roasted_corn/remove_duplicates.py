
def most_frequent(numbers):
    counter = 0
    duplicate = numbers[0]

    for element in numbers:
        curr_frequency = numbers.count(element)

        if curr_frequency > counter:
            counter = curr_frequency
            print(counter)
            duplicate = element

    return duplicate


List = [2, 1, 2, 3, 3, 3, 3, 3, 2, 1, 3]
print(most_frequent(List))
