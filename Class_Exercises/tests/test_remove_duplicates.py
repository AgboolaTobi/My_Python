from unittest import TestCase

from python_assignments.roasted_corn import remove_duplicates


class Test(TestCase):
    def test_most_frequent(self):
        question = [2, 1, 1, 2, 2, 1, 1]
        result = 1
        self.assertEqual(remove_duplicates.most_frequent(question), result)

    def test_most_frequent2(self):
        question = [3, 4, 5, 5]
        result = 5
        self.assertEqual(remove_duplicates.most_frequent(question), result)
