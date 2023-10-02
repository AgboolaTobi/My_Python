from unittest import TestCase
from Java_in_python import array_snacks

class Test(TestCase):
    def test_running_total(self):
        my_array = [1, 2, 3, 4, 5]
        self.assertEqual(" 1 3 6 10 15 ", array_snacks.running_total(my_array))

    def test_running_total_that_has_negative_element(self):
        my_array = [-1, 2, -3, 4, 5]
        self.assertEqual(" -1 1 -2 2 7 ", array_snacks.running_total(my_array))


