from decimal import Decimal, getcontext

from bank_package.exceptions.invalid_deposit_amount_error import InvalidDepositAmountError
from bank_package.exceptions.invalid_pin_error import InvalidPinError
from bank_package.exceptions.invalid_withdrawal_amount_error import InvalidWithdrawalAmount


class Account:
    def __init__(self, name, pin, account_number):
        self.__name = name
        self.__pin = pin
        self.__account_number = account_number
        self.__balance = Decimal('0.00').quantize(Decimal('0.01'))
        getcontext().prec = 2

    def get_account_number(self):
        return self.__account_number

    def deposit(self, amount):
        if amount > 0:
            amount_decimal = Decimal(str(amount))
            self.__balance += amount_decimal
        else:
            raise InvalidDepositAmountError("Kindly enter a valid amount and try again")

    def check_balance(self, pin):
        Account.validate_pin(self, pin)
        return self.__balance

    def validate_pin(self, pin):
        if self.__pin != pin:
            raise InvalidPinError("Invalid pin. Kindly check and try again")
        return self.__pin == pin

    def withdraw(self, amount, pin):
        Account.validate_pin(self, pin)
        if amount <= self.__balance:
            amount_decimal = Decimal(str(amount))
            self.__balance -= amount_decimal
        else:
            raise InvalidWithdrawalAmount(
                "Insufficient funds!")

    def __str__(self):
        return f"""
==========================================
Account Name: {self.__name}        
Account Number : {self.__account_number}
Pin : Undisclosed
Account Balance: {self.__balance}    
==========================================   
"""
