def check_palindrome(numbers):
    number = numbers
    reverse = 0
    while numbers != 0:
        remainder = numbers % 10
        reverse = reverse * 10 + remainder
        numbers = numbers // 10
    if number == reverse:
        return True
    else:
        return False

print(check_palindrome(717))