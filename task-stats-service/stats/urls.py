from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('statslog.urls')),
    path('api/', include('statslog.urls')),
]