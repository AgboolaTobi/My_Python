# list comprehension
numbers = []
for i in range(1, 11):
    numbers.append(i)
print(numbers)

numbers2 = list(range(1, 11))
print(numbers2)


# higher order functions are functions that take another function as part of its argument. am example is the filter
# function. it can be used to sieve a function

def check_even(number):
    answer = 0
    if number % 2 == 0:
        answer = number
    return answer


even_list = filter(check_even, numbers)
print(list(even_list))


result = [i for i in range(1, 11) if i % 2 == 0]
print(result)


this_list = [1, 2, 3, 4, 5, 6]
result1 = [i for i in this_list if i % 2 == 0]
print(result1)

this_list2 = ["agboola", 1, 2, 3, 4, 5, "sola toby", "toby"]
result2 = [i for i in this_list2 if i == "sola" or i == 'toby']
print(result2)
