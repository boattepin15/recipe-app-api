from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """ View for manage recipe APIs"""
    serialzer_class = serializers.RecipeSerialzer
    queryset = Recipe.objects.all()
    authenticaition_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticated]

    def get_queryset(self):
        """ Retrieve recipes for authentocatopm user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')
    