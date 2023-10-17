# or you can use enumerate instead of using range
# enumerate function is used when you're trying to get the index of a particular collection
test_list = [
    [0, 0, 0],
    [0, 0, 0]
 ]

# test_list[0][0] = 5
# test_list[0][1] = 5
# test_list[0][2] = 5
# test_list[1][0] = 5
# test_list[1][1] = 5
# test_list[1][2] = 5
# for i in range(len(test_list)):


for i, value in list(enumerate(test_list)):
    for j, _ in enumerate(value):
        test_list[i][j] = 5
print(test_list)

# vera = list(enumerate(test_list))
# print(vera)
