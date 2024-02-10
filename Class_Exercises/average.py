
# count = 0
# sum = 0
# while count < 10:
#     score = int(input("Enter student score: "))
#     print(count)
#     sum += score
#     count += 1
# average = sum / count
# print(f"And the total score of the 10 students = {sum:.2f}")
# print("The average score of 10 students =", average)
#
# count = 0
# sum = 0
# while True:
#     score = int(input("""
#     Press 101 anytime you wish to end your input!
#     Enter student score and Press 101 to end your input:
#     """))
#     if score == 101:
#         break
#     sum += score
#     count += 1
# average = sum / count
# print(f"And the total score of the students = {sum:.2f}")
# print("The average score of the students =", average)
#
# total = 0
# count = 0
# score = int(input("Enter student score or -1 to stop: "))
# while score != -1:
#     total += score
#     count += 1
#     score = int(input("Enter student score or -1 to stop: "))
# average = total / count
# print("The   average score of the students =", f"{average:.3f}")

count = 1
multiples = 6
while count <= 500:
    multiples += count
    count += 1
    multiples = multiples * count
print(f"{multiples}, end=" "")

multiple = 1
while True:
    multiple = multiple * 6
    if multiple >= 3000:
        break
    print(multiple, end=" ")

multiple = 1
while multiple <= 3000:
    multiple = multiple * 6
    if multiple <= 3000:
        print(multiple, end=" ")
