from django.shortcuts import get_object_or_404, redirect
from .models import Task
import requests
from django.utils.timezone import now

def mark_task_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()

    data = {
        "task_id": task.id,
        "title": task.title,
        "completed_at": str(now())
    }

    try:
        response = requests.post("http://task-stats-service:8000/completed/", json=data)
        response.raise_for_status()
        print("✅ Registro enviado a stats-service")
    except Exception as e:
        print(f"❌ Error al enviar al servicio de stats: {e}")

    return redirect("task_list")