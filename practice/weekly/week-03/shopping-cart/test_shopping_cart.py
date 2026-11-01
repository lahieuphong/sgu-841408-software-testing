import unittest

from shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        """Initialize a new ShoppingCart instance for each test."""
        self.cart = ShoppingCart()

    def test_add_item(self):
        """Test adding a new item to the cart."""
        self.cart.add_item('laptop', 2000, 2)
        items = self.cart.get_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items['laptop']['price'], 2000)
        self.assertEqual(items['laptop']['quantity'], 2)

    def test_add_existing_item(self):
        """Test adding an existing item to the cart."""
        self.cart.add_item('laptop', 2000, 2)
        self.cart.add_item('laptop', 2000, 3)
        items = self.cart.get_items()
        self.assertEqual(items['laptop']['quantity'], 5)

    def test_remove_item(self):
        """Test removing an item from the cart."""
        self.cart.add_item('laptop', 2000, 2)
        self.cart.remove_item('laptop')
        items = self.cart.get_items()
        self.assertEqual(len(items), 0)

    def test_remove_nonexistent_item(self):
        """Test removing an item that doesn't exist in the cart."""
        self.cart.remove_item('laptop')
        items = self.cart.get_items()
        self.assertEqual(len(items), 0)  # No change should be made

    def test_get_total(self):
        """Test calculating the total price of items in the cart."""
        self.cart.add_item('laptop', 2000, 2)
        self.cart.add_item('mouse', 50, 1)
        total = self.cart.get_total()
        self.assertEqual(total, 4050)  # 2 * 2000 + 1 * 50

    def test_get_items(self):
        """Test retrieving the items in the cart."""
        self.cart.add_item('laptop', 2000, 2)
        items = self.cart.get_items()
        self.assertIn('laptop', items)
        self.assertEqual(items['laptop']['price'], 2000)
        self.assertEqual(items['laptop']['quantity'], 2)

if __name__ == '__main__':
    unittest.main()