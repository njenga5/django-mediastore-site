from django.test import TestCase, LiveServerTestCase
from django.urls import reverse
from .models import CustomUser


class CommonopsTests(TestCase, LiveServerTestCase):

    def test_email_password_full_name_phone_number_are_required(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user()

        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(email='test@test.com',
                                           password='testing123', 
                                           full_name='test user')
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(email='test@test.com',
                                           password='testing123', 
                                           phone_number='0712345678')
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(email='test@test.com',
                                           full_name='test user',
                                           phone_number='0712345678')
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(password='testing123', 
                                           phone_number='0712345678',
                                           full_name='test user',)
    
    def test_super_user_is_also_a_staff_and_is_superuser(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                                                email='test@test.com', 
                                                passord='testing123', full_name='test user',
                                                phone_number='0712345678',
                                                is_staff=False,
                                                is_superuser=False)
    
    def test_new_users_are_not_staff_by_default(self):
        user = CustomUser.objects.create_user('test@test.com', 'testing123', 'test user', '0712345678')
        self.assertFalse(user.is_staff)

    def test_new_users_active_by_default(self):
        user = CustomUser.objects.create_user('test@test.com', 'testing123', 'test user', '0712345678')
        self.assertTrue(user.is_active)
    