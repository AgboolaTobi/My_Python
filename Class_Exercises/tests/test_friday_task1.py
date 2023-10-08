from unittest import TestCase
from Class_Exercises import friday_task1


class TestFridayExercise(TestCase):

    def test_triple_function(self):
        my_list = [3, 7, 2, 6, 5]
        useful = friday_task1.triple
        self.assertEqual(friday_task1.triple(my_list), ([27, 343, 8, 216, 125]))
        self.assertEqual(useful([1, 2, 3, 4]), ([1, 8, 27, 64]))
