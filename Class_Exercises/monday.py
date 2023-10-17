# for i in range(2):
#     for j in range(3):
#         j = 2
#         print([i], [j])
#     print()

# for m in range(2):
#     print(m)
#     for n in range(3):
#         print(n)

score = [[25, 50, 75], [40, 50, 60], [70, 65, 80]]
# total1 = 0
# for i in my_list[0]:
#     total1 += i
# print(total1)
# average1 = total1 / len(my_list[0])
# print(average1)
# total2 = 0
# for k in my_list[1]:
#     total2 += k
# print(total2)
# total3 = 0
# for m in my_list[2]:
#     total3 += m
# print(total3)
# average = (total1 + total2 + total3) / len(my_list)
# print(average)

total = 0
overall = 0
student_average = 0
total_student = 0

for v in score:
    student_average = sum(v) / len(v)
    total += sum(v)
    total_student += len(v)
    overall = total / total_student
    print(student_average)
print(overall)
