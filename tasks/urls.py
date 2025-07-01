from django.urls import path
from .views import TaskListCreateView, TaskView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name="task_list_create"),
    path('<pk>/', TaskView.as_view(), name="task_view"),
]