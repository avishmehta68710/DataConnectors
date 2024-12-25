from django.db import models

from core.models import BaseModel
from amazon.models import Marketplace


class SellerProfile(BaseModel):
    """Seller profile model"""

    asin = models.CharField(max_length=255, blank=True, null=True)
    sold_by = models.CharField(max_length=255, blank=True, null=True)
    condition = models.CharField(max_length=255, blank=True, null=True)
    ships_from = models.CharField(max_length=255, blank=True, null=True)
    shipping_price = models.FloatField(blank=True, null=True)
    shipping_currency = models.CharField(max_length=10, blank=True, null=True)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.PROTECT)

    class Meta:
        db_table = '"amazon"."sp"'
        verbose_name = "Seller Profile"
        verbose_name_plural = "Seller Profiles"
