# tests/test_models.py

from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        # Create a new Menu instance
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        # Test the string representation
        self.assertEqual(str(item), "IceCream : 80")
