from rest_framework import serializers
from todo_api import models

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'description', 'due_date', 'completed']
        model = models.Todo