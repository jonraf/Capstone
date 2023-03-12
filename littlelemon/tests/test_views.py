from django.test import TestCase, RequestFactory
from restaurant.models import Menu
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuSerializer


fakeData = [
    {
        'title': 'Manago',
        'price': 25,
        'inventory': 15,
    },
    {
        'title': 'Lemon',
        'price': 17,
        'inventory': 4,
    },
    {
        'title': 'Banana',
        'price': 34,
        'inventory': 24,
    },
]


class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        for mock in fakeData:
            Menu.objects.create(
                title=mock['title'],
                price=mock['price'],
                inventory=mock['inventory']
            )

    def test_getall(self):
        menuitems = Menu.objects.all()
        serialized_menuitems = MenuSerializer(menuitems, many=True)
        request = self.factory.get('restaurant/menu-item/')
        response = MenuItemsView.as_view()(request)

        self.assertEqual(response.data, serialized_menuitems.data)
