from unittest import TestCase

from bank_package.bank import Bank
from bank_package.exceptions.invalid_account_number_error import InvalidAccountNumberError
from bank_package.exceptions.invalid_withdrawal_amount_error import InvalidWithdrawalAmount


class BankTest(TestCase):
    def test_that_bank_can_create_account(self):
        bank = Bank()
        bank.create_account("Tobi", "samuel", "pin")
        self.assertEqual(1, bank.get_total_number_of_existing_customers())

    def test_that_bNak_can_create_multiple_accounts(self):
        bank = Bank()
        bank.create_account("tobi", "samuel", "pin")
        bank.create_account("agboola", "boluwatife", "pin")
        self.assertEqual(2, bank.get_total_number_of_existing_customers())

    def test_that_bank_can_find_account_that_exist_within_it(self):
        bank = Bank()
        bank.create_account("agboola", "toby", "pin")
        find_account_number = bank.find_account_number("0113266571")
        self.assertEqual("0113266571", find_account_number.get_account_number())

    def test_that_for_invalid_account_number_invalid_account_number_exception_is_thrown(self):
        bank = Bank()
        bank.create_account("Agboola", "Toby", "1234")
        with self.assertRaises(InvalidAccountNumberError):
            bank.find_account_number("0113266572")

    def test_that_bank_can_deposit_money_into_an_account_that_exist_within_it(self):
        bank = Bank()
        bank.create_account("Mr Tobi", "Agboola Samuel", "1234")
        bank.deposit("0113266571", 1000)
        self.assertEqual(1000, bank.check_balance("0113266571", "1234"))

    def test_that_bank_can_deposit_into_multiple_account_that_exist_within_it(self):
        bank = Bank()
        bank.create_account("Agboola Tobi", "Samuel", "1234")
        bank.create_account("Agboola Boluwatife", "Charis", "1212")
        bank.deposit("0113266571", 5000)
        bank.deposit("0113266572", 3000)
        self.assertEqual(5000, bank.check_balance("0113266571", "1234"))
        self.assertEqual(3000, bank.check_balance("0113266572", "1212"))

    def test_that_bank_can_withdraw_from_account_that_exists_within_it(self):
        bank = Bank()
        bank.create_account("Agboola", "Tobi", "1234")
        bank.deposit("0113266571", 5000)
        self.assertEqual(5000, bank.check_balance("0113266571", "1234"))
        bank.withdraw("0113266571", 2000, "1234")
        self.assertEqual(3000, bank.check_balance("0113266571", "1234"))

    def test_that_bank_can_withdraw_from_multiple_account_that_exists_within_it(self):
        bank = Bank()
        bank.create_account("agboola", "tobi", "1234")
        bank.create_account("agboola", "Charis", "1212")
        bank.deposit("0113266571", 2000)
        bank.deposit("0113266572", 5000)
        bank.withdraw("0113266571", 500, "1234")
        bank.withdraw("0113266572", 1500, "1212")
        self.assertEqual(1500, bank.check_balance("0113266571", "1234"))
        self.assertEqual(3500, bank.check_balance("0113266572", "1212"))

    def test_that_for_invalid_withdrawal_amount_exception_is_thrown(self):
        bank = Bank()
        bank.create_account("agboola", "tobi", "1212")
        bank.deposit("0113266571", 2000)
        with self.assertRaises(InvalidWithdrawalAmount):
            bank.withdraw("0113266571", 3000, "1212")

    def test_that_bank_can_make_transfer_between_accounts_that_exists_within_it(self):
        bank = Bank()
        bank.create_account("agboola", "tobi", "1212")
        bank.create_account("Oye", "Oyenike", "1313")
        bank.deposit("0113266571", 9000)
        bank.deposit("0113266572", 2000)
        bank.transfer("0113266571", "0113266572", 3000, "1212")
        self.assertEqual(6000, bank.check_balance("0113266571", "1212"))
        self.assertEqual(5000, bank.check_balance("0113266572", "1313"))

    def test_that_bank_can_close_account_that_exists_within_it(self):
        bank = Bank()
        bank.create_account("agboola", "Oluwatobi", "1122")
        bank.create_account("agboola", "Samuel", "1212")
        self.assertEqual(2, bank.get_total_number_of_existing_customers())
        bank.close_account("0113266571", "1122")
        self.assertEqual(1, bank.get_total_number_of_existing_customers())

