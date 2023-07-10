from django.conf import settings
from rest_framework.permissions import BasePermission, SAFE_METHODS


class HaveSecretWordOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if "secret" in request.data and request.data["secret"] == settings.SECRET_WORD:
            return True
        return False
