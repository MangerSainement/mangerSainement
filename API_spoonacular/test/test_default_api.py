"""
    spoonacular API

    The spoonacular Nutrition, Recipe, and Food API allows you to access over thousands of recipes, thousands of ingredients, 800,000 food products, over 100,000 menu items, and restaurants. Our food ontology and semantic recipe search engine makes it possible to search for recipes using natural language queries, such as \"gluten free brownies without sugar\" or \"low fat vegan cupcakes.\" You can automatically calculate the nutritional information for any recipe, analyze recipe costs, visualize ingredient lists, find recipes for what's in your fridge, find recipes based on special diets, nutritional requirements, or favorite ingredients, classify recipes into types and cuisines, convert ingredient amounts, or even compute an entire meal plan. With our powerful API, you can create many kinds of food and especially nutrition apps.  Special diets/dietary requirements currently available include: vegan, vegetarian, pescetarian, gluten free, grain free, dairy free, high protein, whole 30, low sodium, low carb, Paleo, ketogenic, FODMAP, and Primal.  # noqa: E501

    The version of the OpenAPI document: 1.1
    Contact: mail@spoonacular.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from com.spoonacular.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_analyze_recipe(self):
        """Test case for analyze_recipe

        Analyze Recipe  # noqa: E501
        """
        pass

    def test_create_recipe_card_get(self):
        """Test case for create_recipe_card_get

        Create Recipe Card  # noqa: E501
        """
        pass

    def test_search_restaurants(self):
        """Test case for search_restaurants

        Search Restaurants  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()