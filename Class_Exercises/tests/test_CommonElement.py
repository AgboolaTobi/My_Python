from unittest import TestCase

from Class_Exercises.jonathanTasks2024.CommonElement import common


class Test(TestCase):
    def test_common(self):
        first = [2, 3, 5, 6, 7, 8, -1]
        second = [1, 3, 7, 10, 11, 8, -1]

        result = -1
        self.assertEqual(result, common(first, second))

    def test_common2(self):
        third = [5, 4, 11, 13, 9]
        fourth = [9, 11, 15, 1, 14]

        result = 9

        self.assertEqual(9, common(third, fourth))
