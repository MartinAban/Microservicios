from kafka import KafkaProducer
import json

producer = None

def get_producer():
    global producer
    if producer is None:
        producer = KafkaProducer(
            bootstrap_servers='kafka:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    return producer

def publish_task_completed_event(task):
    data = {
        "event": "TASK_COMPLETED",
        "task_id": task.id,
        "title": task.title
    }
    get_producer().send("task-events", value=data)
    print("Evento enviado a Kafka:", data)