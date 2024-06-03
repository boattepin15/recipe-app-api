"""
Serializer for Recipe APIs
"""
from rest_framework import serializers
from core.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipe objects"""
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_miuntes', 'price', 'link', 'description']
        read_only_fields = ['id']

class RecipeDeailSerializer(RecipeSerializer):
    """ Serialzer for recipe detail view."""
    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']