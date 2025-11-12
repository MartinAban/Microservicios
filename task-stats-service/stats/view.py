import requests
from django.http import JsonResponse

def stats_view(request):
    try:
        response = requests.get("http://task-core-service:8000/api/tasks/")
        tasks = response.json()

        total = len(tasks)
        completed = len([t for t in tasks if t.get("completed")])
        pending = total - completed

        return JsonResponse({
            "total": total,
            "completed": completed,
            "pending": pending
        })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)