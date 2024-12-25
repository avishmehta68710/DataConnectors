from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .base_permission import BasePermission
from .base_serializer import BaseSerializer
from .base_pagination import BaseLimitOffsetPagination
from .base_ordering import BaseOrderingFilter


class BaseViewSet(viewsets.ModelViewSet):
    """Base view set"""

    permission_classes = [BasePermission]
    serializer_class = BaseSerializer
    pagination_class = BaseLimitOffsetPagination
    filter_backends = [BaseOrderingFilter, DjangoFilterBackend]
    # authentication_classes = [JWTAuthentication]
    http_method_names = ["get", "post", "put", "head", "options"]

    def destroy(self, request, *args, **kwargs):
        self.soft_destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def soft_destroy(self, request, *args, **kwargs):
        """
        when overriding destroy function that needs additional logic after deletion, use `self.soft_destroy()`
        rather than `super().destroy()`
        for example, in api3/patient/main.py,

        def destroy(self, request, *args, **kwargs):
          self.soft_destroy(request, *args, **kwargs)
          obj = self.get_object()
          # delete log
          Patient.objects.filter(id=obj.id).delete()
          ...
        """
        obj = self.get_object()
        if hasattr(obj, "deleted_on"):
            obj.deleted_on = timezone.now()
            obj.save()
