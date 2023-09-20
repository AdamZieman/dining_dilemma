# tests/test_restaurants.py

"""
Unit Tests for the Restaurants Class

This module contains unit tests for the `Restaurants` class from the `src.backend.restaurants` module.
The tests cover various aspects of the `Restaurants` class's functionality.

To run the tests, use the following command from the project root directory:
python -m unittest -v tests.test_restaurants

Prerequisites:
- Ensure that the `src.restaurants` module is correctly installed or available in your Python environment.
"""

from restaurants import Restaurants
import unittest

# Run tests from the project root directory with the command:
# python -m unittest -v tests.test_restaurants

class TestRestaurants(unittest.TestCase):
    # Tests constructor
    def test_parameter_dine_in_init(self):
        self.assertIsNotNone(Restaurants("dine-in"))

    def test_parameter_take_out_init(self):
        self.assertIsNotNone(Restaurants("take-out"))

    def test_init_raises_assertion_error(self):
        with self.assertRaises(AssertionError):
            invalid_restaurants = Restaurants("invalid_method")



    # Tests generate_random_list function for dine-in
    def test_parameterless_generate_random_list_length_for_dine_in(self):
        dine_in_restaurants = Restaurants(Restaurants.DINE_IN)
        random_dine_in = dine_in_restaurants.generate_random_list()
        self.assertEqual(len(random_dine_in), 1)

    def test_parameter1_generate_random_list_length_for_dine_in(self):
        dine_in_restaurants = Restaurants(Restaurants.DINE_IN)
        random_dine_in = dine_in_restaurants.generate_random_list(1)
        self.assertEqual(len(random_dine_in), 1)

    def test_parameter_max_length_generate_random_list_length_for_dine_in(self):
        dine_in_restaurants = Restaurants(Restaurants.DINE_IN)
        max_length = len(dine_in_restaurants.restaurants_list)
        random_dine_in = dine_in_restaurants.generate_random_list(max_length)
        self.assertEqual(len(random_dine_in), max_length)

    def test_parameter_exceeds_length_generate_random_list_length_for_dine_in(self):
        dine_in_restaurants = Restaurants(Restaurants.DINE_IN)
        max_length = len(dine_in_restaurants.restaurants_list)
        with self.assertRaises(AssertionError):
            invalid_restaurants = dine_in_restaurants.generate_random_list(max_length + 1)

    def test_parameter_receeds_length_generate_random_list_length_for_dine_in(self):
        dine_in_restaurants = Restaurants(Restaurants.DINE_IN)
        with self.assertRaises(AssertionError):
            invalid_restaurants = dine_in_restaurants.generate_random_list(0)

    

    # Tests generate_random_list function for take-out
    def test_parameterless_generate_random_list_length_for_take_out(self):
        take_out_restaurants = Restaurants(Restaurants.TAKE_OUT)
        random_take_out = take_out_restaurants.generate_random_list()
        self.assertEqual(len(random_take_out), 1)

    def test_parameter1_generate_random_list_length_for_take_out(self):
        take_out_restaurants = Restaurants(Restaurants.TAKE_OUT)
        random_take_out = take_out_restaurants.generate_random_list(1)
        self.assertEqual(len(random_take_out), 1)

    def test_parameter_max_length_generate_random_list_length_for_take_out(self):
        take_out_restaurants = Restaurants(Restaurants.TAKE_OUT)
        max_length = len(take_out_restaurants.restaurants_list)
        random_take_out = take_out_restaurants.generate_random_list(max_length)
        self.assertEqual(len(random_take_out), max_length)

    def test_parameter_exceeds_length_generate_random_list_length_for_take_out(self):
        take_out_restaurants = Restaurants(Restaurants.TAKE_OUT)
        max_length = len(take_out_restaurants.restaurants_list)
        with self.assertRaises(AssertionError):
            invalid_restaurants = take_out_restaurants.generate_random_list(max_length + 1)

    def test_parameter_receeds_length_generate_random_list_length_for_take_out(self):
        take_out_restaurants = Restaurants(Restaurants.TAKE_OUT)
        with self.assertRaises(AssertionError):
            invalid_restaurants = take_out_restaurants.generate_random_list(0)

    

    # Test if get_restaurants_list returns the correct list
    def test_get_restaurants_list_for_dine_in(self):
        dine_in_restaurants = Restaurants(Restaurants.DINE_IN)
        self.assertEqual(dine_in_restaurants.get_restaurants_list(), Restaurants.RESTAURANTS_LISTS[Restaurants.DINE_IN])

    def test_get_restaurants_list_for_take_out(self):
        take_out_restaurants = Restaurants(Restaurants.TAKE_OUT)
        self.assertEqual(take_out_restaurants.get_restaurants_list(), Restaurants.RESTAURANTS_LISTS[Restaurants.TAKE_OUT])



if __name__ == "__main__":
    unittest.main()