def average_scores(scores):
    return sum(scores) / len(scores)

exam_score = []
for score in range(10):
    score = int(input("Enter your exam score:"))
    exam_score.append(score)
    sum += score