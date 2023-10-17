from unittest import TestCase
from Class_Exercises import biggest_odd


class TestBiggestOdd(TestCase):

    def test_biggest_odd(self):
        numbers = '23569'
        result = '9'
        # rain = input("Enter numbers ")
        # rains = rain
        self.assertEqual(biggest_odd.biggest_odds(numbers), result)
        # self.assertEqual(biggest_odd.biggest_odds(rains), '9')
