#
# x = 0
# y = 1
#
# total = x + y
# while x < 50:
#     print(x, end=' ')
#     x = y
#     y = total
#     total = x +y

# def square():
#     numz = int(input("Enter a number:"))
#     result = numz * numz
#     return result
#
#
# print(square())
# print(square())
#
# def check_palindrome(numbers):
#     number = numbers
#     reverse = 0
#     while numbers != 0:
#         remainder = numbers % 10
#         reverse = reverse * 10 + remainder
#         numbers = numbers // 10
#     if number == reverse:
#         return True
#     else:
#         return False
#
#
# print(check_palindrome(797))


List = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]

def custom_sorted(ls: List) -> List:
    for i in range(0, len(List)):
        for j in range(i+1, len(List)):
            if List[i] >= List[j]:
                List[i], List[j] = List[j], List[i]
    return List


print(custom_sorted(List))
