from .models import Task
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .retry_and_circuit_breaker import retry_and_circuit_breaker
from .kafka_producer import publish_task_completed_event
import requests


@csrf_protect
def task_list_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title, completed=False)
        return redirect("task_list")

    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def delete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("task_list")


@csrf_protect
def complete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()

    #Evento asincrónico
    publish_task_completed_event(task)

    #Llamada HTTP sincrónica con retry + circuit breaker
    @retry_and_circuit_breaker()
    def send_completed_task():
        return requests.post("http://stats-load-balancer/api/stats/record/", json={
            "task_id": task.id,
            "title": task.title
        })

    try:
        send_completed_task()
    except Exception as e:
        print(f"Error al enviar tarea completada a stats-service vía load balancer: {e}")

    return redirect("task_list")
