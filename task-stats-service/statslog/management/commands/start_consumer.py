from django.core.management.base import BaseCommand
from statslog.kafka_consumer import start_kafka_consumer

class Command(BaseCommand):
    help = "Inicia el consumidor Kafka"

    def handle(self, *args, **kwargs):
        start_kafka_consumer()
