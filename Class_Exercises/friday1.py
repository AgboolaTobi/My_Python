# numbers = []
# for i in range(0, 10):
#     scores = input("enter number: ")
#     numbers.append(scores)
#
#     def multiply(*numbers):
#         product = 2
#         for number in numbers:
#             product *= number
#         return product
#
# print(multiply(numbers))

def average_of_score(my_scores, sum_of_score):
    sum_of_score = sum_of_score + scores
    average = sum_of_score / len(my_scores)
    return average


my_scores = []
sum_of_score = 0
average = 0
for scores in range(0, 10):
    scores = int(input("Enter score: "))
    my_scores.append(scores)
print(my_scores)

print("The average of the scores = ", average_of_score(my_scores, sum_of_score))
