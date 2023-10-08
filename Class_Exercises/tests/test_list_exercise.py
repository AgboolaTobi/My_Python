from unittest import TestCase
from Class_Exercises import list_exercise


class TestListExercise(TestCase):

    def test_that_add_function_exist(self):
        list_exercise.add_function([15, 20, 25, 20, 10, 5])

    def test_add_function(self):
        self.assertEquals(list_exercise.add_function([15, 20, 25, 20, 10, 5]), 95)
        self.assertEquals(list_exercise.add_function([1, 2, 3, 4, 5]), 15)

    def test_multiplication(self):
        self.assertEquals(list_exercise.multiply_function([15, 20, 25, 20, 10, 5]), 7500000)
        self.assertEquals(list_exercise.multiply_function([2, 3, 4, 5]), 120)

    def test_for_largest_number(self):
        self.assertEquals(list_exercise.find_largest_number([15, 20, 25, 20, 10, 5]), 25)
        self.assertEquals(list_exercise.find_largest_number([2, 3, 4, 5]), 5)

    def test_for_smallest_number(self):
        self.assertEquals(list_exercise.find_smallest_number([15, 20, 25, 20, 10, 5]), 5)
        self.assertEquals(list_exercise.find_smallest_number([2, 3, 4, 5]), 2)

    def test_for_no_duplicate1(self):
        self.assertEqual(list_exercise.no_duplicate_number([15, 20, 25, 20, 10, 5]), [15, 20, 25, 10, 5])
