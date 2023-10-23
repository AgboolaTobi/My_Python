from unittest import TestCase
from Class_Exercises import sorting_dictionary


class TestSortingDictionary(TestCase):

    def test_ascending(self):
        sample = {2: 4, 1: 1, 3: 9, 5: 25, 4: 16}
        result = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        self.assertEqual(sorting_dictionary.sort_dictionary(sample), result)

    def test_descending(self):
        sample = {2: 4, 1: 1, 3: 9, 5: 25, 4: 16}
        result = {5: 25, 4: 16, 3: 9, 2: 4, 1: 1}
        self.assertEqual(sorting_dictionary.reverse_dictionary(sample), result)

    def test_adding_key(self):
        my_dictionary = {1: 10, 2: 20}
        result = {1: 10, 2: 20, 3: 30}
        self.assertEqual(sorting_dictionary.add_key(my_dictionary, 3, 30), result)
