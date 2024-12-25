from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
from sp_api.util import retry

from core.utils import BaseViewSet
from amazon.models import SellerProfile
from .serializer import SellerProfileSerializer, SellerProfileListSerializer
from .permission import SellerProfilePermission
from .filters import SellerProfileFilterSet


class SellerProfileViewSet(BaseViewSet):
    """Seller Profile viewset"""
    queryset = SellerProfile.objects.all()
    serializer_class = SellerProfileSerializer
    permission_classes = [SellerProfilePermission]
    filterset_class = SellerProfileFilterSet
    ordering = ["-updated_on", "created_on"]
    http_method_names = ["get", "post"]
    
    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        match self.action:
            case "list" | "retrieve":
                return SellerProfileListSerializer(*args, **kwargs)
            case _:
                return super().get_serializer(*args, **kwargs)
    
    @method_decorator(ratelimit(key='ip', rate='10/m', method='POST', block=True))
    @retry()
    def create(self, request, *args, **kwargs):
        """Create product"""
        return super().create(request, *args, **kwargs)
