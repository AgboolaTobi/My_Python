numbers = int(input("Enter a number: "))
reverse = 0
while numbers != 0:
    remainder = numbers % 10
    reverse = reverse * 10 + remainder
    number = numbers // 10
    if numbers == reverse:
        print(reverse)
    if numbers != reverse:
        print("Number is not palindrome")
    numbers += 1

