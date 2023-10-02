from unittest import TestCase
from Java_in_python import array_snacks


class Test(TestCase):
    def test_reverse_array(self):
        my_array = [1, 2, 4, 5, 3]
        my_array2 = [3, 5, 4, 2, 1]
        self.assertEqual(my_array2, array_snacks.reverse_list(my_array))

    def test_reverse_array2(self):
        my_array = [1, -2, -4, 3]
        my_array2 = [3, -4, -2, 1]
        self.assertEqual(my_array2, array_snacks.reverse_list(my_array))
