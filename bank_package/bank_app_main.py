import sys
from decimal import Decimal

from bank_package.bank import Bank

my_bank = Bank()


def create_account():
    while True:
        user_first_name = input("Enter your first_name: ")

        if not user_first_name.isalpha():
            print("Your first name should consist of only letters! ")
        else:
            break
    while True:
        user_last_name = input("Enter your last name: ")
        if not user_last_name.isalpha():
            print("Your last name should consist of only letters! ")
        else:
            break
    while True:
        password = input("Create your unique password: ")
        if not password.isdigit() or len(password) != 4:
            print("Your password must consist of only digits and must be 4 characters long")
        else:
            break

    account = my_bank.create_account(user_first_name, user_last_name, password)
    print(f"""Account successfully created
    Here's your account number: {account}
    You're up for a thrilling experience!
    """)
    bank_menu()


def deposit():
    account_number = input("Enter your account number: ")
    while True:
        amount_entered = input("Enter amount: ")
        if not amount_entered.isdigit():
            print("Your deposit amount must contain positive numbers only!")
        else:
            amount = Decimal(amount_entered)
            break
    try:
        my_bank.deposit(account_number, amount)
        print(f"{amount} has been successfully deposited into {account_number} .")
        bank_menu()

    except Exception as exception:
        print(exception)
        bank_menu()


def withdraw():
    account_number = input("Enter your account number: ")
    while True:
        amount_entered = input("Enter amount: ")

        if not amount_entered.isdigit():
            print("Your withdrawal amount must contain positive numbers only.")
        else:
            amount = Decimal(amount_entered)
            break

    password = input("Enter your password: ")

    try:
        my_bank.withdraw(account_number, amount, password,)
        print(f"""
        You have successfully withdrawn {amount}
        Account Balance: {my_bank.check_balance(account_number, password):.0f}
        """)
        bank_menu()
    except Exception as exception:
        print(exception)
        bank_menu()


def check_balance():
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")

    try:

        print(f"Account balance: {my_bank.check_balance(account_number, password):.0f}")
        bank_menu()
    except Exception as exception:
        print(exception)
        bank_menu()


def transfer():
    transfer_from_account = input("Enter the account number you wish to transfer from: ")
    transfer_to_account = input("Enter the account number you wish to transfer to: ")

    while True:
        amount_str = input("Enter the amount you wish to transfer: ")
        if not amount_str.isdigit():
            print("Your transfer amount must contain only positive numbers!")
        else:
            amount = Decimal(amount_str)
            break
    account_password = input("Enter your unique password: ")

    try:
        my_bank.transfer(transfer_from_account, transfer_to_account, amount, account_password)
        print(
            f"Your transfer of {amount} to {transfer_to_account} was successful \n Your account balance: {my_bank.check_balance(transfer_from_account, account_password)}")

    except Exception as exception:
        print(exception)
        bank_menu()


def close_account():
    account_number = input("Enter your account number: ")
    account_password = input("Enter your password: ")
    while True:
        try:
            my_bank.find_account_number(account_number)
            my_bank.close_account(account_number, account_password)
            break
        except Exception as exception:
            print(exception)
            bank_menu()


def bank_menu():
    user_response = input("""
    ===================================
    Unified Bank Of Nations(UBN)
    ===================================
    1 -> Create Account
    2 -> Make Deposit
    3 -> Make withdrawal
    4 -> Check balance
    5 -> Make Transfer
    6 -> Close account
    7 -> Exit
    """)
    match user_response:
        case "1":
            create_account()
            bank_menu()
        case "2":
            deposit()
            bank_menu()
        case "3":
            withdraw()
            bank_menu()
        case "4":
            check_balance()
            bank_menu()
        case "5":
            transfer()
            bank_menu()
        case "6":
            close_account()
            bank_menu()
        case "7":
            sys.exit(2)


class BankApp:
    bank_menu()
