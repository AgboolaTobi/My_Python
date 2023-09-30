my_scores = []
sum_of_score = 0


def average_of_score(my_scores, sum_of_score, ):
    sum_of_score = sum_of_score + scores
    average = sum_of_score / len(my_scores)
    return average


for scores in range(0, 10):
    scores = int(input("Enter score: "))
    my_scores.append(scores)

print("The average of the scores = ", average_of_score(my_scores, sum_of_score))
