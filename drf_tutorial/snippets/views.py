from django.contrib.auth.models import User
from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions


class SnippetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # Override perform_create to modify how instance is saved
    # allowing the association of snippets with users
    def perform_create(self, serializer):
        serializer.save(owner.self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class UserList(generics.ListAPIView):
    """ Read-only user class-based views. """
    queryset = User.objects.all()
    serializer_class = UserSerializer()

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = SnippetSerializer