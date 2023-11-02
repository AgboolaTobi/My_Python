from unittest import TestCase
from Java_in_python import domino_pizza


class Test(TestCase):
    def test_order_list(self):
        result = "Total number of slices ordered: 40 \nThe total number of boxes bought: 4.0 \n The total cost of order: 20000.0\nTotal number of left over: 0"

        self.assertEqual(domino_pizza.order_list(), result)
