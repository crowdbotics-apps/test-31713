from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from apps.api.v1.serializers import AppSerializer
from apps.models import App

User = get_user_model()


class AppTests(APITestCase):
    
    def setUp(self):
        
        self.app_url = reverse('apps:app-list')
        
        self.user_obj = User.objects.create(
            first_name='test',
            last_name='user',
            username='testuser',
            email='testuser@email.com',
            password='testpassword',
        )
        
        self.client.force_authenticate(self.user_obj)
        
        
    def test_create_app(self):
        
        """
        Ensure we can create a new app object.
        """
        
        data = {
            "name": "NewApp",
            "desc": "NewApp description."
        }
        
        response = self.client.post(self.app_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_retrieve_user_apps(self):
        
        """
        Ensure user can retrieve his apps.
        """
        
        response = self.client.get(self.app_url)
        
        apps = App.objects.filter(user=self.user_obj)
        serializer = AppSerializer(apps, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
    def test_delete_user_apps(self):
        
        """
        Ensure user can delete his app.
        """
            
        app = App.objects.create(
            name="Test App",
            desc="NewApp description.",
            user=self.user_obj
            )
        
        self.app_detail_url = reverse('apps:app-detail', kwargs={'pk': app.pk})
        
        response = self.client.delete(self.app_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_update_user_apps(self):
        
        """
        Ensure user can update his app.
        """        
        app = App.objects.create(
            name="Test App",
            desc="NewApp description.",
            user=self.user_obj
            )
        
        self.app_detail_url = reverse('apps:app-detail', kwargs={'pk': app.pk})
        
        data = {
            "name": "Updated Test App",
            "desc": "NewApp description."
        }
        
        
        response = self.client.put(self.app_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)