my_scores = []
sum_of_score = 0
average = 0
for count in range(0, 10):
    scores = int(input("Enter score: "))
    my_scores.append(scores)
    length_of_scores = len(my_scores)
    sum_of_score = sum_of_score + scores
    average = sum_of_score / len(my_scores)
print("The scores are:", my_scores)
print("The sum of scores = ", sum_of_score)
print("The average", average)
print("The length of the scores= ", length_of_scores)
for i in range(0, len(my_scores)):
    for j in range(i+1, len(my_scores)):
        if my_scores[i] >= my_scores[j]:
            my_scores[i], my_scores[j] = my_scores[j], my_scores[i]

print("Arranged score:", my_scores)
print("The maximum score is ", my_scores[-1])
print("The minimum score = ", my_scores[0])
