from django.urls import path
from .views import task_list_view, delete_task_view, complete_task_view

urlpatterns = [
    path('tasks/', task_list_view, name='task_list'),
    path('tasks/delete/<int:task_id>/', delete_task_view, name='delete_task'),
    path('tasks/complete/<int:task_id>/', complete_task_view, name='complete_task'),
]