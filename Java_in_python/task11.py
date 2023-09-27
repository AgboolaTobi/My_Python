my_scores = []
for count in range(0, 10):
    scores = int(input("Enter score: "))
    my_scores.append(scores)
print("Unsorted score:", my_scores)
print("The length of the scores= ", len(my_scores))
for i in range(0, len(my_scores)):
    for j in range(i+1, len(my_scores)):
        if my_scores[i] >= my_scores[j]:
            my_scores[i], my_scores[j] = my_scores[j], my_scores[i]

print("Sorted score:", my_scores)
print("The largest score is ", my_scores[-1])
