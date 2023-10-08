from unittest import TestCase

from python_assignments import corn_flakes


class PythonAssignments(TestCase):

    def test_reverse(self):
        tuple1 = (10, 20, 30, 40, 50)
        self.assertEqual(corn_flakes.reverse(tuple1), (50, 40, 30, 20, 10))
        self.assertEqual(corn_flakes.reverse((2, 4, 5, 6, 7)), (7, 6, 5, 4, 2))

    def test_single_tuple(self):
        tuple1 = (2,)
        self.assertEqual(corn_flakes.singleton(tuple1), (2,))

    def test_unpacking(self):
        tuple1 = (15, 25, 60, 50, 30, 40, 45, 55)
        tuple2 = (3, 6, 9, 12)
        tuple3 = (-1, 3, 5, -7)
        self.assertEqual(corn_flakes.unpacking(tuple1), (55, 15))
        self.assertEqual(corn_flakes.unpacking(tuple2), (12, 3))
        self.assertEqual(corn_flakes.unpacking(tuple3), (-7, -1))

    def test_sorting(self):
        tuple4 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
        self.assertEqual(corn_flakes.Sort_Tuple(tuple4),  (('c', 11), ('a', 23), ('d', 29), ('b', 37)))
