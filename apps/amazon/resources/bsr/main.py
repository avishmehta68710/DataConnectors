from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
from sp_api.util import retry

from core.utils import BaseViewSet
from amazon.models import Bsr
from .serializer import BsrSerializer, BsrListSerializer
from .permission import BsrPermission
from .filters import BsrFilterSet


class BsrViewSet(BaseViewSet):
    """Marketplace viewset"""
    queryset = Bsr.objects.all()
    serializer_class = BsrSerializer
    permission_classes = [BsrPermission]
    filterset_class = BsrFilterSet
    ordering = ["-updated_on", "created_on"]
    http_method_names = ["get", "post"]
    
    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        match self.action:
            case "list" | "retrieve":
                return BsrListSerializer(*args, **kwargs)
            case _:
                return super().get_serializer(*args, **kwargs)
    
    @method_decorator(ratelimit(key='ip', rate='10/m', method='POST', block=True))
    @retry()
    def create(self, request, *args, **kwargs):
        """Create product"""
        return super().create(request, *args, **kwargs)
