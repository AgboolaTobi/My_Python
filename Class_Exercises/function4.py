def number(n):
    x = 0
    y = 1
    total = x + y
    while x < 50:
        print(x, end=' ')
        x = y
        y = total
        total = x + y
    return total


print(number())