# src/backend/resaurants.py

from random import sample

class Restaurants:
    """
    Represents a collection of restaurants with dine-in and take-out options.

    Attributes:
        DINE_IN (str): Constant representing the 'dine-in' order method.
        TAKE_OUT (str): Constant representing the 'take-out' order method.
        RESTAURANTS_LISTS (dict): A dictionary containing restaurant lists for different order methods.
    """
    DINE_IN = "dine-in"
    TAKE_OUT = "take-out"
    RESTAURANTS_LISTS = {
        DINE_IN: [
            {
                "name": "Milwaukee Burger Company",
                "reason": "cajon fries, cheese curds, and burgers"
            },
            {
                "name": "Ricardo's Pizza",
                "reason": "pasta"
            },
            {
                "name": "Olive Garden",
                "reason": "bread sticks with unlimited dipping sauce, and pasta"
            },
            {
                "name": "Cheesecake Factory",
                "reason": "bread and a wide variety of food"
            },
            {
                "name": "Red Lobster",
                "reason": "seafood"
            },
            {
                "name": "Buffalo Wild Wings",
                "reason": "wings"
            },
            {
                "name": "Texas Roadhouse",
                "reason": "cinnamon honey butter with bread, and steak"
            },
            {
                "name": "El Beso Restaurante & Cartina",
                "reason": "chips, salsa, and Mexican food"
            },
            {
                "name": "El Senorial Mexican Restaurant",
                "reason": "authentic Mexican food"
            },
            {
                "name": "Tu Casa Mexican Restaurant & Bar",
                "reason": "authentic Mexican food"
            },
            {
                "name": "Hacienda Chivolin",
                "reason": "Mexican seafood"
            },
            {
                "name": "Japanica",
                "reason": "Japanese hibachi"
            },
            {
                "name": "Kyoto",
                "reason": "sushi"
            },
            {
                "name": "New China Buffet",
                "reason": "Chinese buffet"
            }
        ],
        TAKE_OUT: [
            {
                "name": "Chick-fil-A",
                "reason": "chicken sandwiches and waffle fries"
            },
            {
                "name": "Culver's",
                "reason": "burgers, cheese curds, and onion rings"
            },
            {
                "name": "Wendy's",
                "reason": "chicken nuggets and french fries"
            },
            {
                "name": "Subway",
                "reason": "custom made subs"
            },
            {
                "name": "Cousins Subs",
                "reason": "quality subs"
            },
            {
                "name": "Panera Bread",
                "reason": "soup and a sandwiches"
            },
            {
                "name": "Noodles and Company",
                "reason": "noodles or pasta"
            },
            {
                "name": "Di Stefano's Pizza Place",
                "reason": "pizza"
            },
            {
                "name": "Super No. 1 Chinese",
                "reason": "Kung Pao Chicken, egg rolls, and crab rangoon"
            }
        ]
    }

    def __init__(self, order_method):
        """
        Initialize the Restaurants class with the specified order method.
        Args:
            order_method (str): Either 'dine-in' or 'take-out'.
        """
        assert order_method in [Restaurants.DINE_IN, Restaurants.TAKE_OUT]
        self.restaurants_list = Restaurants.RESTAURANTS_LISTS[order_method]

    def generate_random_list(self, count=1):
        """
        Generate a random list of restaurants from the specified order method.
        Args:
            count (int): Number of restaurants to generate.
        Returns:
            list: A list of random restaurant entries.
        """
        assert 1 <= count <= len(self.restaurants_list)
        return sample(self.restaurants_list, count)

    def get_restaurants_list(self):
        """
        Get the list of restaurants for the specified order method.
        Returns:
            list: A list of restaurant entries.
        """
        return self.restaurants_list

