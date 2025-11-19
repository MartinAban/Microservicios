import requests
from django.http import JsonResponse

AUTH_SERVICE_URL = "http://auth-service:8002/auth/service-token"
SERVICE_ID = "task-stats-service"
SERVICE_SECRET = "stats-secret"

def get_jwt_token():
    payload = {
        "service_id": SERVICE_ID,
        "service_secret": SERVICE_SECRET
    }
    try:
        response = requests.post(AUTH_SERVICE_URL, json=payload)
        response.raise_for_status()
        return response.json().get("access")
    except requests.RequestException as e:
        print("Error al obtener token:", e)
        return None

def stats_view(request):
    try:
        token = get_jwt_token()
        if not token:
            return JsonResponse({"error": "No se pudo obtener el token"}, status=500)

        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.get("http://task-core-service:8000/api/tasks/", headers=headers)
        response.raise_for_status()
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