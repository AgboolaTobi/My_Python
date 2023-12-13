# def number(n):
#     x = 0
#     y = 1
#     total = x + y
#     while x < 50:
#         print(x, end=' ')
#         x = y
#         y = total
#         total = x + y
#     return total
#
#
# print(number())

def power(number, raised_to_power):
    the_power = number ** raised_to_power
    return the_power


print(power(2, -1))
print(power(5, 4))
