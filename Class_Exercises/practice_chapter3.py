# grade = int(input("Enter grade: "))
# if 70 < grade < 100:
#     print(grade, "-Distinction")
# elif 60 < grade < 70:
#     print(grade, "Excellent")
# elif 50 < grade < 60:
#     print(grade, "Average")
# elif 40 < grade < 50:
#     print(grade, "passed")
# else:
#     print(grade, "Fail")

#
# product =7
# while product <= 1000:
#     product *= 7
# print(product, end=" ")
#
# number = [2, 3, 5, 1, 20]
# print(sum(number))
# The above printed the 'sum' using the inbuilt sum function

# To print the sum without using the inbuilt function sum

# total = 0
# number1 = [2, 3, 5, 1, 20]
# for number1 in number1:
#     total = total + number1
# print(total, end=" ")
#
# number1 = [2, 3, 5, 1, 20]
# product = 1
# sum = 0
# for number1 in number1:
#     product = 3 * number1
#     sum = 0 + product
#     print("Product= ", product, end=" ")
# print("Sum =", sum, end=" ")

sum_of_grades = 0
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]
length = len(grades)
print(length)

for grades in grades:
    sum_of_grades += grades
print(sum_of_grades)
average = sum_of_grades / length
print(average)
