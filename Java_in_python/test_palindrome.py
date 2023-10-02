from unittest import TestCase
from Java_in_python import array_snacks

class Test(TestCase):

    def test_palindrome(self):
        my_array = "abba"
        self.assertTrue(array_snacks.is_palindrome(my_array))

    def test_not_palindrome(self):
        my_array = "python"
        self.assertFalse(array_snacks.is_palindrome(my_array))
