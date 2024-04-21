"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model



class ModelTests(TestCase):
    """ Test models."""

    def test_create_user_with_emil_scc(self):
        """ Test Creating Email is scc"""

        email = "test@gmail.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

