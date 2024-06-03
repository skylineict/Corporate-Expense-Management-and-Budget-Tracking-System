# tests.py
from authencation.models import User
from  register import register_users
from rest_framework.test import APIClient, APITestCase
from rest_framework.exceptions import AuthenticationFailed


class RegisterUsersTest(APITestCase):
    def setUp(self):
        self.email = 'test@example.com'
        self.first_name = 'Test'
        self.last_name = 'User'
        self.provider = 'google'
        User.objects.create(email=self.email, first_name=self.first_name, last_name=self.last_name, auth_user_provider=self.provider)
        print('account created ')

    def test_user_exists_with_same_provider(self):
        # Test case where user exists with the same provider
        response = register_users(self.provider, self.email, self.first_name, self.last_name)
        # Assert response or behavior

    def test_user_exists_with_different_provider(self):
        # Test case where user exists with a different provider
        with self.assertRaises(AuthenticationFailed):
            register_users('facebook', self.email, self.first_name, self.last_name)

    def test_user_does_not_exist(self):
        # Test case where user does not exist
        new_email = 'new@example.com'
        response = register_users(self.provider, new_email, self.first_name, self.last_name)
        # Assert response or behavior
