from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Dirección del servicio A
TASK_SERVICE_URL = "http://localhost:8000/api/tasks/"

@app.route("/stats")
def get_task_stats():
    try:
        response = requests.get(TASK_SERVICE_URL)
        response.raise_for_status()
        tasks = response.json()

        total = len(tasks)
        completed = len([t for t in tasks if t["completed"]])
        pending = total - completed

        return jsonify({
            "total_tasks": total,
            "completed_tasks": completed,
            "pending_tasks": pending
        })

    except requests.RequestException as e:
        return jsonify({"error": "No se pudo conectar al servicio A", "details": str(e)}), 503


if __name__ == "__main__":
    app.run(port=5000, debug=True)