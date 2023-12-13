from decimal import getcontext

from bank_package.account import Account
from bank_package.exceptions.invalid_account_number_error import InvalidAccountNumberError


def create_customer_name(first_name, last_name):
    return first_name + " " + last_name


class Bank:
    def __init__(self):
        self.accounts = []
        getcontext().prec = 2
        self.count_number_of_customer = 1

    def create_account(self, first_name, last_name, pin):
        generate_customer_name = create_customer_name(first_name, last_name)
        generate_account_number = Bank.account_number(self)
        account = Account(generate_customer_name, pin, generate_account_number)
        self.accounts.append(account)

        self.count_number_of_customer += 1
        return account

    def account_number(self):
        return f"011326657{self.count_number_of_customer}"

    def get_total_number_of_existing_customers(self):
        return len(self.accounts)

    def find_account_number(self, account_number):
        for value in self.accounts:
            if value.get_account_number() == account_number:
                return value
        raise InvalidAccountNumberError(f"{account_number} not found")

    def deposit(self, account_number, amount):
        account_number = self.find_account_number(account_number)
        account_number.deposit(amount)

    def check_balance(self, account_number, pin):
        account_number = self.find_account_number(account_number)
        return account_number.check_balance(pin)

    def withdraw(self, account_number, amount, pin):
        account_number = self.find_account_number(account_number)
        account_number.withdraw(amount, pin)

    def transfer(self, from_account, to_account, amount, pin):
        sender_account = self.find_account_number(from_account)
        receiver_account = self.find_account_number(to_account)
        sender_account.withdraw(amount, pin)
        receiver_account.deposit(amount)

    def close_account(self, account_number, pin):
        account_number = self.find_account_number(account_number)
        Account.validate_pin(account_number, pin)
        self.accounts.remove(account_number)
