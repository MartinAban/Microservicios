import json
from kafka import KafkaConsumer
from .models import CompletedTaskLog

def start_kafka_consumer():
    consumer = KafkaConsumer(
        'task-events',
        bootstrap_servers='kafka:9092',
        group_id='stats-group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        enable_auto_commit=True
    )

    print("Escuchando eventos en 'task-events'...")

    for message in consumer:
        data = message.value
        print(f" Evento recibido: {data}")

        CompletedTaskLog.objects.create(
            task_id=data["task_id"],
            title=data["title"]
        )