from unittest import TestCase
from Java_in_python import array_snacks

class Test(TestCase):
    def test_oddly(self):
        my_array = [1, 2, 3, 4, 5]
        my_array2 = [2, 4]
        self.assertEqual(my_array2, array_snacks.odd_position_element(my_array))

    def test_negative_element_in_oddly_positioned(self):
        my_array = [1, -2, 3, 4, 5]
        my_array2 = [-2, 4]
        self.assertEqual(my_array2, array_snacks.odd_position_element(my_array))

