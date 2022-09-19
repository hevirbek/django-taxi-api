from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AccountTests(APITestCase):
    def test_create_taxi(self):
        """
        Ensure we can create a new taxi.
        """
        url = reverse('api/taxi')
        data = {
            'plate': '02 DEF 02',
            'driver': 2,
            'coordX': 25,
            'coordY': 45,
            'active': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_taxi(self):
        """
        Ensure we can get a taxi.
        """
        url = reverse('api/taxi/1')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_taxi(self):
        """
        Ensure we can update a taxi.
        """
        url = reverse('api/taxi/1')
        data = {
            'plate': '02 DEF 02',
            'driver': 2,
            'coordX': 25,
            'coordY': 45,
            'active': False
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_taxi(self):
        """
        Ensure we can delete a taxi.
        """
        url = reverse('api/taxi/1')
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
