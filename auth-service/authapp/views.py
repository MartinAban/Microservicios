from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import jwt
from datetime import datetime, timedelta

# Credenciales de servicios (simples, hardcodeadas para la práctica)
SERVICE_CREDENTIALS = {
    "task-core-service": "core-secret",
    "task-stats-service": "stats-secret",
}

class ServiceTokenView(APIView):
    """
    POST /auth/service-token
    body: { "service_id": "task-core-service", "service_secret": "core-secret" }
    """
    def post(self, request):
        service_id = request.data.get("service_id")
        service_secret = request.data.get("service_secret")

        if not service_id or not service_secret:
            return Response(
                {"detail": "service_id and service_secret are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        expected_secret = SERVICE_CREDENTIALS.get(service_id)
        if expected_secret is None or expected_secret != service_secret:
            return Response(
                {"detail": "Invalid service credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        #JWT
        now = datetime.utcnow()
        payload = {
            "sub": service_id,
            "type": "service",
            "iat": now,
            "exp": now + timedelta(minutes=30),
        }

        token = jwt.encode(
            payload,
            settings.JWT_SIGNING_KEY,
            algorithm="HS256"
        )

        return Response({"access": token})