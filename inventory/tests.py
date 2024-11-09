
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Item
from django.contrib.auth.models import User

class InventoryTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.item_url = reverse('item-list')

    def test_create_item(self):
        response = self.client.post(self.item_url, {'name': 'Test Item', 'quantity': 10, 'description': 9.99})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_items(self):
        response = self.client.get(self.item_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_item(self):
        item = Item.objects.create(name='Item 1', quantity=5, description=12.50)
        response = self.client.put(reverse('item-detail', args=[item.id]), {'name': 'Updated Item', 'quantity': 15, 'price': 10.00})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_item(self):
        item = Item.objects.create(name='Item to Delete', quantity=3, description=5.00)
        response = self.client.delete(reverse('item-detail', args=[item.id]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



