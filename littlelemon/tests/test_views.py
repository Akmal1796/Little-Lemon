from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restaurant.models import Menu
import json
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu_item1 = Menu.objects.create(title="Pizza Margherita", price=8.99, inventory=10)
        self.menu_item2 = Menu.objects.create(title="Caesar Salad", price=6.99, inventory=15)
        self.menu_item3 = Menu.objects.create(title="Spaghetti Carbonara", price=10.99, inventory=20)

    def test_getall(self):
        url = reverse('MenuItemsView')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many = True)
        self.assertEqual(response.data, serializer.data)