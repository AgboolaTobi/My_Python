from unittest import TestCase
from Java_in_python import conversions


class TestConversion(TestCase):

    def test_decimal_to_binary(self):
        number = 56
        result = '111000'
        self.assertEqual(conversions.decimal_to_binary(number), result)

    def test_binary_to_decimal(self):
        binary = 111000
        self.assertEqual(conversions.binary_to_decimal(binary), 56)
