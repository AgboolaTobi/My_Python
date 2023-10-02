from unittest import TestCase
from Java_in_python import array_snacks


class Test(TestCase):
    def test_check_element(self):
        my_array = [1, 2, 3, 4, 5]
        self.assertTrue(array_snacks.check_element(my_array, 3))

    def test_negative_element(self):
        my_array = [1, -3, 4]
        self.assertTrue(array_snacks.check_element(my_array, -3))

    def test_that_element_is_absent(self):
        my_array = [1, 3, 2, 4, 5]
        self.assertFalse(array_snacks.check_element(my_array, 9))
