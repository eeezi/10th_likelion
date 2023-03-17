from rest_framework import viewsets
from todo_api import models
from .serializers import TodoSerializer

class TodoViewset(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer