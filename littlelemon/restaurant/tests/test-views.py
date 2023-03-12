from django.test import TestCase
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(
            name='Hamburger',  price=8, inventory=20)
        self.menu2 = Menu.objects.create(
            name='Veggie Burger',  price=9, inventory=30)

    def test_getall(self):
        response = self.client.get(('menu/'))
        menus = Menu.objects.all()
        serialized_data = [{'id': menu.id, 'name': menu.name, 'price': menu.price, 'inventory':
                            menu.inventory} for menu in menus]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), serialized_data)
