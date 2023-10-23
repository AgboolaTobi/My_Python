def decimal_to_binary(number):
    answer = ""
    if number == 0:
        return 0
    while number > 0:
        answer += str(number & 1)
        number = number >> 1

    answer = answer[::-1]

    return answer


def binaryToDecimal(number):
    return int(number, 2)


def binary_to_decimal(binary):
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


print(binaryToDecimal('111000'))
print(binary_to_decimal(111000))
