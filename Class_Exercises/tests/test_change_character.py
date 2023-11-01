from unittest import TestCase
from Class_Exercises import change_character


class Test(TestCase):
    def test_change_occurrence(self):
        sample1 = 'restart'
        sample2 = 'rest'
        self.assertEqual(change_character.change_occurrence(sample1), 'resta$t')
        self.assertEqual(change_character.change_occurrence(sample2), 'rest')
