# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
from authencation.models import User
# from test_setup import SetupTest
from .test_setup import SetupTest

import pdb


class RegistrationViewTests(SetupTest):
    def test_user_cannot_register_without_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)
      

# class RegistrationViewTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.url = reverse('singup')

#     def test_registration_successful(self):
#         data = {
#             'email': 'testuser@example.com',
#             'username': 'testuser',
#             'password': 'testpassword123'
#         }
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertIn('message', response.data)
#         self.assertIn('data', response.data)
#         self.assertTrue(User.objects.filter(email='testuser@example.com').exists())

#     def test_registration_invalid_data(self):
#         data = {
#             'email': 'invalid-email',
#             'username': '',
#             'password': 'short'
#         }
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn('email', response.data)
#         self.assertIn('username', response.data)
#         self.assertIn('password', response.data)

#     def test_registration_missing_fields(self):
#         data = {
#             'email': 'testuser@example.com'
#         }
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn('password', response.data)
#         self.assertIn('username', response.data)



# class LoginViewTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.url = reverse('login')  # Ensure this matches the URL name in your urls.py
#         self.user = User.objects.create_user(
#             email='testuser@example.com',
#             username='testuser',
#             password='testpassword123'
#         )
#         self.user.is_verifiedemail = True
#         self.user.save()

#     def test_login_successful(self):
#         data = {
#             'email': 'testuser@example.com',
#             'password': 'testpassword123'
#         }
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('refresh', response.data)
#         self.assertIn('access', response.data)

#     def test_login_invalid_email_or_password(self):
#         data = {
#             'email': 'wrong@example.com',
#             'password': 'testpassword123'
#         }
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn('error', response.data)

#         data = {
#             'email': 'testuser@example.com',
#             'password': 'wrongpassword'
#         }
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn('error', response.data)

#     def test_login_unverified_email(self):
#         self.user.is_verifiedemail = False
#         self.user.save()
        
#         data = {
#             'email': 'testuser@example.com',
#             'password': 'testpassword123'
#         }
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#         self.assertIn('message', response.data)

#     def test_login_missing_fields(self):
#         data = {
#             'email': 'testuser@example.com'
#         }
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#         data = {
#             'password': 'testpassword123'
#         }
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)