from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .serializers import TaskSerializer
from .models import Task

class TaskViewSet(ModelViewSet):
    search_fields = ['name', 'description','status', 'due_by']
    filter_backends = (filters.SearchFilter,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
