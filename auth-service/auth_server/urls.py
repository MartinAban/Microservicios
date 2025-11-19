from django.contrib import admin
from django.urls import path
from authapp.views import ServiceTokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/service-token', ServiceTokenView.as_view(), name='service-token'),
]