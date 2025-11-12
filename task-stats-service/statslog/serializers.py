from rest_framework import serializers
from .models import CompletedTaskLog

class CompletedTaskLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedTaskLog
        fields = '__all__'