from unittest import TestCase
from Class_Exercises import character_frequency


class Test(TestCase):
    def test_frequency(self):
        string = 'google.com'
        result = {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
        self.assertEqual(character_frequency.frequency(string), result)

    def test_frequency1(self):
        string = 'google.com'
        result = {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
        self.assertEqual(character_frequency.character_frequency_correction(string), result)

    def test_frequency2(self):
        string = 'google.com'
        result = {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
        self.assertEqual(character_frequency.character_frequency_correction2(string), result)
