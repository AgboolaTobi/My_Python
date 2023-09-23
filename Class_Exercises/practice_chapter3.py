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
#
# product =7
# while product <= 1000:
#     product *= 7
# print(product, end=" ")
#
# number = [2, 3, 5, 1, 20]
# print(sum(number))
# The above printed the 'sum' using the inbuilt sum function
#
# To print the sum without using the inbuilt function sum
#
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
#
# sum_of_grades = 0
# grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]
# length = len(grades)
# print(length)
#
# for grades in grades:
#     sum_of_grades += grades
# print(sum_of_grades)
# average = sum_of_grades / length
# print(average)
#
#
# total = 0
# count = 0
# grades = int(input("Enter the grades(Enter -1 to end your input: "))
# while grades != -1:
#     total += grades
#     count += 1
#     grades = int(input("Enter the grades (enter -1 to end your input): "))
#     if grades != 0:
#         average = total/count
#         print(average)
#     else:
#         print("No grades were entered")


passes = 0
fails = 0
for students in range(10):
    result = int(input("Enter student result (Enter 1 for pass and 2 for fail):"))
    if result == 1:
        passes += 1
    else:
        fails += 1

print("Passed:", passes)
print("Failed:", fails)

if passes >= 8:
    print("Credit to instructor!")

for i in range(2):
    first = int(input("Enter first integer:"))
    second = int(input("Enter second integer:"))
    if first % 2 == 0:
        print("first number is even", first)
    else:
        print("first number is odd", first)
    if second % 2 == 0:
        print("second is even",second)
    else:
        print("second is odd", second)
