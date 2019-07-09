from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import TodoItem
from api.serializers import TodoSerializer
from api.permissions import IsOwnerOrReadOnly
# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    """
    A set of endpoints to list, create, update and delete To Do items.
    """

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = TodoSerializer

    def get_queryset(self):
        return TodoItem.objects.filter(author=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
