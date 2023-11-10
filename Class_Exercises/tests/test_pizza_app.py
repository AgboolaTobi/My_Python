from unittest import TestCase
from Java_in_python import pizza_app


class Test(TestCase):
    def test_that_large_pizza_size_box_can_be_ordered(self):
        self.assertEqual(pizza_app.pizza_size(), 10)

    def test_that_medium_pizza_size_box_can_be_ordered(self):
        self.assertEqual(pizza_app.pizza_size(), 6)

    def test_that_small_pizza_size_box_can_be_ordered(self):
        self.assertEqual(pizza_app.pizza_size(), 4)


class TestTwo(TestCase):
    def test_hunger_level_of_super_hungry_guests(self):
        self.assertEqual(pizza_app.hunger_level(), 4)

    def test_hunger_level_of_normal_hungry_guests(self):
        self.assertEqual(pizza_app.hunger_level(), 2)

    def test_hunger_level_of_classic_hungry_guests(self):
        self.assertEqual(pizza_app.hunger_level(), 1)
