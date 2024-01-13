from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import House, Seller  # Import your custom user model
from rest_framework_simplejwt.tokens import RefreshToken


class HouseTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Seller.objects.create_user(username='testuser', password='testpass')
        self.house = House.objects.create(title='Test House', seller=self.user, total_price=1000000, price_per_meter=20000, city='Test City', address='Test Address', description='Test Description')

        # Get a token for the test user and use it to authenticate the client. (It doesn't work !)
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')

    def test_list_houses(self):
        response = self.client.get(reverse('list-houses'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_user_houses(self):
        response = self.client.get(reverse('list-user-houses'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user_house(self):
        data = {'title': 'New House', 'total_price': 2000000, 'price_per_meter': 40000, 'city': 'New City', 'address': 'New Address', 'description': 'New Description'}
        response = self.client.post(reverse('create-user-house'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_user_house(self):
        response = self.client.delete(reverse('delete-user-house', kwargs={'pk': self.house.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_user_house(self):
        data = {'title': 'Updated House'}
        response = self.client.put(reverse('update-user-house', kwargs={'pk': self.house.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_city_houses(self):
        response = self.client.get(reverse('list-city-houses', kwargs={'city': 'Test City'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        