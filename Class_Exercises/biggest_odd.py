def biggest_odd(list_of_numbers):
    odds = []
    for number in list_of_numbers:
        if int(number) % 2 != 0:
            odds.append(number)
    highest = odds[0]
    for odd_number in odds:
        if odd_number > highest:
            highest = odd_number
    return highest


numbers = '27668765'

print(biggest_odd(numbers))


highest_odd = max(filter(lambda number: int(number) % 2 == 1, numbers))


print(highest_odd, numbers)


# Created my own max function and called it in the biggest odds function
def maximum(my_numbers):
    maxi = my_numbers[0]
    for i in my_numbers:
        if i > maxi:
            maxi = i
    return maxi


def biggest_odds(numbers1):
    return maximum([number for number in numbers1 if int(number) % 2 != 0])


def smallest_odd(given_list):
    global value
    odd = []

    for number in given_list:
        if number % 2 == 1:
            odd.append(number)

    smallest = odd[0]
    for value in odd:
        if value < smallest:
            value = smallest

    return value


given_list = [1, 2, 3, 4, 5, 9, 6, 7]
print(smallest_odd(given_list))
print(given_list[1:7])