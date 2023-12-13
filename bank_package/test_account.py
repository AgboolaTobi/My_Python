from unittest import TestCase
from bank_package.account import *


class AccountTest(TestCase):
    def test_that_account_can_be_deposited_into_and_balance_can_be_checked(self):
        account = Account("full _name", "pin", "1")
        account.deposit(Decimal(1000))
        self.assertEqual(Decimal(1000), account.check_balance("pin"))

    def test_that_invalid_deposit_amount_throws_invalid_amount_exception(self):
        account = Account("full_name", "pin", "1")
        with self.assertRaises(InvalidDepositAmountError):
            account.deposit(-1000)
            account.deposit(0)

    def test_that_account_can_make_more_deposit(self):
        account = Account("full_name", "pin", "1")
        account.deposit(2000)
        account.deposit(3000)
        account.deposit(5000)
        self.assertEqual(Decimal(10000), account.check_balance("pin"))

    def test_that_for_invalid_pin_account_throws_invalid_pin_exception(self):
        account = Account("full_name", "pin", "1")
        with self.assertRaises(InvalidPinError):
            account.check_balance("pins")

    def test_that_account_can_be_withdrawn_from(self):
        account = Account("Agboola Tobi", "1234", "1")
        account.deposit(5000)
        account.withdraw(2000, "1234")
        self.assertEqual(3000, account.check_balance("1234"))

    def test_that_my_account_will_throw_an_exception_if_amount_to_withdraw_exceeds_balance(self):
        account = Account("Mr Sikiru Ayinlade", "babanla", "1")
        account.deposit(1000)
        with self.assertRaises(InvalidWithdrawalAmount):
            account.withdraw(9000, "babanla")
