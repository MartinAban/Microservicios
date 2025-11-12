from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CompletedTaskLog
from .serializers import CompletedTaskLogSerializer

class CompletedTaskReceiver(APIView):
    def post(self, request):
        serializer = CompletedTaskLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registro guardado"}, status=201)
        return Response(serializer.errors, status=400)

class StatsView(APIView):
    def get(self, request):
        total = CompletedTaskLog.objects.count()
        return Response({
            "completed_tasks": total
        })