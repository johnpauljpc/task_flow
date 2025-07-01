from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOfTask
from .filters import TaskFilter

from .models import Task
from .serializers import TaskSerializer

# Create your views here.
class TaskListCreateView(ListCreateAPIView):
    """
    This allows authenticated users to create Tasks and also view a list of their tasks.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = TaskFilter

    def get_queryset(self):
        logged_in_user = self.request.user
        return Task.objects.filter(owner = logged_in_user )
    

class TaskView(RetrieveUpdateDestroyAPIView):
    """
    Allows authenticated  users to Retrieve, Update, and Delete a given task. 
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOfTask]
    def get_queryset(self):
        logged_in_user = self.request.user
        return Task.objects.filter(owner = logged_in_user )