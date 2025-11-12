from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("""
        <html>
        <head>
            <title>MicroTasks</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 100px;
                    background-color: #f4f4f4;
                }
                h1 {
                    color: #333;
                }
                a.button {
                    display: inline-block;
                    padding: 12px 24px;
                    font-size: 16px;
                    color: white;
                    background-color: #4CAF50;
                    border-radius: 8px;
                    text-decoration: none;
                    margin-top: 20px;
                    transition: background-color 0.3s ease;
                }
                a.button:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <h1>Bienvenido a tu lista de tareas</h1>
            <p>Haz clic para ver tus tareas</p>
            <a href="/api/tasks/" class="button">Ver Lista de Tareas</a>
        </body>
        </html>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('tasks/', home_view),
]