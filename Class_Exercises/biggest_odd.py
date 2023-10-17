def biggest_odd(list_of_numbers):
    odds = []
    for i in list_of_numbers:
        if int(i) % 2 != 0:
            odds.append(i)
    highest = odds[0]
    for j in odds:
        if j > highest:
            highest = j
    return highest


numbers = '92668765'

# print(biggest_odd(numbers))


highest_odd = max(filter(lambda x: int(x) % 2 == 1, numbers))

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
