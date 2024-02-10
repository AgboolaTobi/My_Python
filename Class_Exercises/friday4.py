# When the addition function is called,it will produce an error because it will be expecting one argument
def addition(scores):
    return sum(scores)


# the * enables this to take as many parameters(scores) and run the function to take inputs until user is satisfied and then finds the average of the scored inputed.
def average_score(*scores):
    total = 0
    for _ in scores:
        total += 1
        return total / len(scores)


print(average_score(2, 3, 5))

#
# print(addition(3, 5, 6, 7, 5, 3, 2, 1, 23, 4))
