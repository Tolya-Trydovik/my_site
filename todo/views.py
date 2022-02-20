from rest_framework import viewsets, permissions

from .models import Todo
from .serializers import TodoSerializers


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializers