from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
from sp_api.util import retry

from core.utils import BaseViewSet
from amazon.models import Marketplace
from .serializer import MarketplaceSerializer
from .permission import MarketplacePermission
from .filters import MarketplaceFilterSet


class MarketplaceViewSet(BaseViewSet):
    """Marketplace viewset"""

    queryset = Marketplace.objects.all()
    serializer_class = MarketplaceSerializer
    permission_classes = [MarketplacePermission]
    filterset_class = MarketplaceFilterSet
    ordering = ["-updated_on", "created_on"]
    http_method_names = ["get", "post"]

    @method_decorator(ratelimit(key="ip", rate="1/m", method="POST", block=True))
    @retry(tries=3)
    def create(self, request, *args, **kwargs):
        """Create product"""
        return super().create(request, *args, **kwargs)
