from django.urls import path, include
from rest_framework.routers import DefaultRouter

from amazon.resources import (
    MarketplaceViewSet,
    InventoryViewSet,
    RnrViewSet,
    PromotionsViewSet,
    BsrViewSet,
    SellerProfileViewSet,
    ProductViewSet,
)

router = DefaultRouter()
router.register(r"marketplace", MarketplaceViewSet)
router.register(r"inventory", InventoryViewSet)
router.register(r"rnr", RnrViewSet)
router.register(r"promotions", PromotionsViewSet)
router.register(r"bsr", BsrViewSet)
router.register(r"sp", SellerProfileViewSet)
router.register(r"product", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
