from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from api.models import TodoItem
from api.serializers import TodoSerializer
from rest_framework_swagger import renderers
# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    """
    A set of endpoints to list, create and delete To Do items.
    """
    
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def get_queryset(self):
        return TodoItem.objects.filter(author=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        if instance.author == self.request.user:
            instance.delete()

    def perform_update(self, serializer):
        pass
