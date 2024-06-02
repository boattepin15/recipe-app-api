"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal
from core import models


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

    def test_create_recipe(self):
        """ Test Creating a recipe successful"""
        user = get_user_model().objects.create_user(
            "test@gmail.com",
            "testpass1234"
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title = "Simple recipe name",
            time_miuntes=5,
            price=Decimal('5.50'),
            description="Simple recipe Description"
        )

        self.assertEqual(str(recipe), recipe.title)

