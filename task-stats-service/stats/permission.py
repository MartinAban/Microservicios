from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsServiceToken(BasePermission):
    """
    Permite solo tokens emitidos para microservicios (con 'type': 'service').
    """

    def has_permission(self, request, view):
        user = request.user
        token = getattr(user, 'token', None)

        if token is None:
            raise PermissionDenied("No JWT token found")

        token_type = token.payload.get('type', None)
        if token_type != 'service':
            raise PermissionDenied("Token is not a service token")

        return True