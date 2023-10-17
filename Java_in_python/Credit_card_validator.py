def validator(n):
    validate_list = []

    for i in n:
        validate_list.append(int(i))

    for i in range(0, len(n), 2):
        [i] = [i] * 2
        if [i] >= 10:
            [i] = [i] // 10 + [i] % 10

    if sum() % 10 == 0:
        print('This a valid credit card')

    else:
        print('This is not valid credit card')


def card_number():
    result = ''
    while True:
        try:
            result = input('Please enter the 16 digit credit card number : ')

            if not (len(result) == 16) or not type(int(result) == int):
                raise Exception

        except Exception:
            print(
                'That is not a proper credit card number. \nMake sure you are entering digits not characters and all the 16 digits.')
            continue

        else:
            break

    return result


def goagain():
    return input('Do you want to check again? (Yes/No) : ').lower()[0] == 'y'


def main():
    while True:

        result = cardnumber()
        validator(result)

        if not goagain():
            break


if __name__ == '__main__':
    main()
