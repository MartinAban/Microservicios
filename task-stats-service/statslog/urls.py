from django.urls import path
from .views import CompletedTaskReceiver, StatsView

urlpatterns = [
    path('api/notify/', CompletedTaskReceiver.as_view(), name='notify'),
    path('api/stats/', StatsView.as_view(), name='stats'),
]