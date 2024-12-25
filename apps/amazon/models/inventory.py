from django.db import models

from core.models import BaseModel
from amazon.models import Marketplace


class Inventory(BaseModel):
    asin = models.CharField(max_length=255, blank=True, null=True)
    is_qty_limit_set = models.BooleanField(blank=True, null=True)
    marketplace = models.ForeignKey(
        Marketplace, on_delete=models.PROTECT, blank=True, null=True
    )
    merchant_id = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = '"amazon"."inventory"'
        verbose_name = "Inventory"
        verbose_name_plural = "Inventory"
