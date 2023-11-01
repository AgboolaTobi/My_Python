from unittest import TestCase
from Class_Exercises import unique


class Test(TestCase):
    def test_unique(self):
        numbers = [1, 3, 2, 5, 3, 4, 6, 4, 6, 9, 8, 2, 10, 8, 12, 15, 10, 6, 14]
        result = [2, 4, 6, 8, 10, 12, 14]
        self.assertEqual(unique.unique(numbers), result)
