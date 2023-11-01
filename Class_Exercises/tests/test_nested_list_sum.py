from unittest import TestCase
from Class_Exercises import nested_list_sum


class Test(TestCase):
    def test_sum_list(self):
        numbers = [[2, 4, 5, 6], [2, 3, 5, 6]]
        result = 33
        self.assertEqual(nested_list_sum.sum_list(numbers), result)
