my_scores = []
for count in range(0, 10):
    scores = int(input("Enter score: "))
    my_scores.append(scores)
print("Unarranged score list:", my_scores)
print("The length of the scores= ", len(my_scores))
for i in range(0, len(my_scores)):
    for j in range(i+1, len(my_scores)):
        if my_scores[i] <= my_scores[j]:
            my_scores[i], my_scores[j] = my_scores[j], my_scores[i]
# this list is rearranged in descending order,the largest will be the first element in the list.
print("Arranged list score:", my_scores)
print("The largest score is ", my_scores[0])
