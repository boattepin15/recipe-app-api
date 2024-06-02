"""
Serializer for Recipe APIs
"""

from rest_framework import serializers
from core.models import Recipe


class RecipeSerialzer(serializers.ModelSerializer):
    """ Serializer or recipe"""

    class Mate:
        model = Recipe
        fields = ['id', 'title', 'time_miuntes', 'price', 'link']
        read_only_fields = ['id']