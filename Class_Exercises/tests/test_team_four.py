from unittest import TestCase
from Class_Exercises import friday_team4


class TestFridayTeam4(TestCase):

    def test_that_list_exist(self):
        my_team = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertEqual(friday_team4.mylist(), my_team)

    def test_for_odd_numbers(self):
        odd_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        self.assertEqual(friday_team4.odd_list(), odd_list)

    def test_for_doubling_element(self):
        odd_doubled = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38]
        self.assertEqual(friday_team4.double(), odd_doubled)

    def test_that_element_between_4_and_7_have_been_changed(self):
        my_team = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        result1 = [2, 6, 10, 14, 0, 0, 0, 0, 34, 38]
        self.assertEqual(friday_team4.change_element(my_team), result1)

    def test_function_can_concatenate_two_list(self):
        list1 = ['w', 'a', 'th', 'xplo']
        list2 = ['e', 're', 'e', 'rers']
        list3 = ['we', 'are', 'the', 'xplorers']
        self.assertEqual(friday_team4.concatenate(list1, list2), list3)
