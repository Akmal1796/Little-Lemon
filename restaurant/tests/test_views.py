from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.menu_item_1 = Menu.objects.create(title="Burger", price=120, inventory=50)
        self.menu_item_2 = Menu.objects.create(title="Pizza", price=250, inventory=30)
        self.menu_item_3 = Menu.objects.create(title="Pasta", price=180, inventory=40)
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        self.client = APIClient()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_all_menu(self):
        response = self.client.get('/restaurant/menu/')
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
