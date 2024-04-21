from rest_framework import generics, authentication, permissions
from user.serializers import UserSerializer, AuthTokenSerializers  # Renamed serializer for clarity
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken  # Corrected import


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializers
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES  # Corrected attribute name

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]  # Corrected 'permissions_classes' to 'permission_classes'

    def get_object(self):
        """Retrieve and return the authenticated user."""
        # Ensure the request has an authenticated user associated with it
        return self.request.user