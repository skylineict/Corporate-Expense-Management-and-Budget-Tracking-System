from rest_framework.test import APIClient, APITestCase
from django.urls import reverse


class SetupTest(APITestCase):
    def setUp(self):
        self.register_url = reverse('singup')
        self.login_url = reverse('login')

        user_data = {

            "email": "email@gmail.com",
            "username": "username",
            "password": "password"
        }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()