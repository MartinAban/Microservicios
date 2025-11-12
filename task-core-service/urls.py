from django.urls import path
from .views import task_list, mark_task_completed

urlpatterns = [
    path('', task_list, name="task_list"),
    path('tasks/<int:task_id>/complete/', mark_task_completed, name="mark_task_completed"),
]