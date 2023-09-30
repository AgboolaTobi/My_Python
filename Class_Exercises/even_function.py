# def even():
#     even_numbers = []
#     for count in range(0, 51, 2):
#         if count == 20:
#             break
#         even_numbers.append(count)
#     print(even_numbers)
#     average = sum(even_numbers) / len(even_numbers)
#     return average
#
#
# print(even())
#
my_scores = []
for count in range(0, 10):
    scores = int(input("Enter score: "))
    my_scores.append(scores)
# print("Unsorted score:", my_scores, end=" ")
# print("The length of the scores= ", len(my_scores))
for i in range(0, len(my_scores)):
    print(i, end=" ")
    for j in range(i+1, len(my_scores)):
        print(j)
