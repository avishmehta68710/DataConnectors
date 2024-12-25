from rest_framework.permissions import (
    BasePermission as DRFBasePermission,
)


class BasePermission(DRFBasePermission):
    """Base permission"""

    def has_permission(self, request, view):
        """request view permission check fallback"""
        return True
