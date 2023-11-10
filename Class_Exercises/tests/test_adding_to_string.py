from unittest import TestCase
from Class_Exercises import adding_to_string


class Test(TestCase):
    def test_add_sting_to_string(self):
        word = "abc"
        result = "abcing"
        self.assertEqual(adding_to_string.add_sting_to_string(word), result)

    def test_add_sting_to_string2(self):
        word = "it"
        result = "it"
        self.assertEqual(adding_to_string.add_sting_to_string(word), result)

    def test_add_sting_to_string3(self):
        word = "string"
        result = "stringly"
        self.assertEqual(adding_to_string.add_sting_to_string(word), result)

