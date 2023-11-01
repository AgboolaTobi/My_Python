from unittest import TestCase
from python_assignments import weekend_cornflakes


class Test(TestCase):
    def test_split_list(self):
        sample_output = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        result = [10, 75, 20, 30, 15], [5, 40, 25, 40, 35]
        self.assertEqual(weekend_cornflakes.split_list(sample_output), result)

    def test_that_frequent_elements_are_Picked(self):
        sample_input = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
        sample_output = [1, 2, 5]
        self.assertEqual(weekend_cornflakes.frequency_of_elements(sample_input), sample_output)

    def test_that_difference_between_max_and_min_can_be_returned(self):
        sample = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        result = 70
        self.assertEqual(weekend_cornflakes.difference_of_max_and_min(sample), result)
        self.assertEqual(weekend_cornflakes.difference_of_max_and_min2(sample), result)

    def test_list_to_dictionary1(self):
        sample_input = ['apple', 'banana', 'coconut']
        output = {'a': 'apple', 'b': 'banana', 'c': 'coconut'}
        self.assertEqual(weekend_cornflakes.list_to_dictionary_correction(sample_input), output)

    def test_list_to_dictionary2(self):
        sample_input = ['apple', 'banana', 'coconut', 'about']
        output = {'a': 'apple', 'b': 'banana', 'c': 'coconut',  'A': 'about'}
        self.assertEqual(weekend_cornflakes.list_to_dictionary_correction(sample_input), output)
