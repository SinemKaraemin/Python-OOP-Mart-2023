# from ..shopping_cart import ShoppingCart

import unittest
from unittest.mock import patch
from ..shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def test_init(self):
        shopping_cart = ShoppingCart("Test", 100.0)
        self.assertEqual(shopping_cart.shop_name, "Test")
        self.assertEqual(shopping_cart.budget, 100.0)
        self.assertEqual(shopping_cart.products, {})

    def test_shop_name_valid(self):
        with self.assertRaises(ValueError) as er:
            ShoppingCart('test1', 100)
        self.assertEqual('Shop must contain only letters and must start with capital letter!', str(er.exception))

    def test_add_to_cart(self):
        shop = ShoppingCart("MyShop", 200.0)
        shop.add_to_cart('product_name1', 99)
        self.assertEqual('product_name2 product was successfully added to the cart!', shop.add_to_cart('product_name2', 98))
        self.assertEqual({'product_name1': 99, 'product_name2': 98}, shop.products)

    def test_add_to_cart_should_raise_error(self):
        shop = ShoppingCart("Test", 200)
        with self.assertRaises(ValueError) as er:
            shop.add_to_cart('test_product', 100)
        self.assertEqual('Product test_product cost too much!', str(er.exception))

    def test_remove_from_cart(self):
        shop = ShoppingCart('Test', 200)
        shop.add_to_cart('product_name1', 99)
        shop.add_to_cart('product_name2', 98)
        actual = shop.remove_from_cart('product_name1')
        expected = 'Product product_name1 was successfully removed from the cart!'
        self.assertEqual(expected, actual)
        self.assertEqual({'product_name2': 98}, shop.products)

    def test_add(self):
        first = ShoppingCart("Test", 200.0)
        first.add_to_cart('from_first', 1)
        second = ShoppingCart("SecondTest", 100)
        second.add_to_cart('from_second', 2)
        merged = first.__add__(second)
        self.assertEqual('TestSecondTest', merged.shop_name)
        self.assertEqual(300, merged.budget)
        self.assertEqual({'from_first': 1, 'from_second': 2}, merged.products)

    def test_buy_products_with_valid_data(self):
        shop = ShoppingCart('Test', 200)
        shop.add_to_cart('product_name1', 99)
        shop.add_to_cart('product_name2', 98)
        self.assertEqual('Products were successfully bought! Total cost: 197.00lv.', shop.buy_products())

    def test_buy_products_should_raise_error(self):
        shop = ShoppingCart('Test', 20)
        shop.add_to_cart('product_name1', 99)
        with self.assertRaises(ValueError) as er:
            shop.buy_products()
        expected = 'Not enough money to buy the products! Over budget with 79.00lv!'
        actual = str(er.exception)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
