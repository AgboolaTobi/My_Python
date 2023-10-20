from unittest import TestCase
from Class_Exercises import equal_string


class TestEqualString(TestCase):

    def test_equal_string(self):
        number1 = 'lovgewff23'
        number = 'evol23gwff'
        self.assertTrue(equal_string.equal_string(number, number1))
