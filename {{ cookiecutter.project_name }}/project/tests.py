from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import UserProfile

class UserRegistrationTests(TestCase):
    def test_register_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Register')

    def test_register_view_post(self):
        User = get_user_model()
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'SuperSecret123',
            'password2': 'SuperSecret123',
        })
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='testuser').exists())

class UserProfileTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='profileuser', password='testpass')

    def test_profile_view_requires_login(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_profile_view_post(self):
        self.client.login(username='profileuser', password='testpass')
        response = self.client.post(reverse('profile'), {'bio': 'Hello world!'})
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.bio, 'Hello world!')

class LoginLogoutTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='loginuser', password='testpass')

    def test_login(self):
        response = self.client.post(reverse('login'), {'username': 'loginuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        self.client.login(username='loginuser', password='testpass')
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)
