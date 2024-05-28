# from rest_framework.test import APITestCase
# from authencation.models import User


# from rest_framework.test import APITestCase
# from authencation.models import User

# class Usermodeltest(APITestCase):
#     def test_create_user(self):
#         # Create a user
#         user = User.objects._create_user('monskeys@gmail.com', 'monskeys', 'Monoskey@@')
#         print(user.email)
#         self.assertEqual(user.email,"monskeys@gmail.com")
#         self.assertEqual(user.username,"monskeys")
#         self.assertFalse(user.is_staff)
#         self.assertTrue(user.is_active)
#         self.assertFalse(user.is_superuser) # Assuming it's False by default

    
#     def test_raise_value_if_username_is_empty(self):
#         self.assertRaises(ValueError, User.objects.create_user,email='', username="tototot", password='Monoskey@@')


#     def test_create_superuser(self):
#         superuser = User.objects.create_superuser('skylineict23@gmail.com', 'Moskey@@@@#')
#         if superuser:
#             print('your email is', superuser.email)

#         self.assertEqual(superuser.email,"skylineict23@gmail.com")
#         self.assertTrue(superuser.is_staff)
#         self.assertTrue(superuser.is_superuser)

#     def test_create_superuser_status(self):
#         with self.assertRaisesMessage(ValueError,'Superuser must have is_staff=True.'):
#             User.objects.create_superuser('skylineict23@gmail.com', 'Moskey@@@@#', is_staff=False )
    

#     def test_create_superuser_status_supperuser(self):
#         with self.assertRaisesMessage(ValueError,'Superuser must have is_superuser=True.'):
#             User.objects.create_superuser('skylineict23@gmail.com', 'Moskey@@@@#',is_superuser=False )










