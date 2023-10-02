from unittest import TestCase
from Java_in_python import array_snacks


class Test(TestCase):
    def test_largest1(self):
        my_array = [1, 2, 3, 4, 5, 6]
        self.assertEqual(6, array_snacks.largest_element(my_array))

    def test_largest2(self):
        my_array = [-2, -4, -1, -6]
        self.assertEqual(-1, array_snacks.largest_element(my_array))
