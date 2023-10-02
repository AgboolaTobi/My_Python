from unittest import TestCase
from Java_in_python import array_snacks


class Test(TestCase):
    def test_alternate_combination(self):
        myArray = [1, 2, 3]
        myArray2 = ['a', 'b', 'c']
        self.assertEqual(array_snacks.alternate_combination(myArray, myArray2))
