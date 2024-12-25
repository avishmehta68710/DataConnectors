from django.db import models

from core.models import BaseModel
from amazon.models import Marketplace


class Promotions(BaseModel):
    asin = models.CharField(max_length=10)
    brand = models.CharField(max_length=255, null=True, blank=True)
    deal_badge = models.CharField(max_length=255, null=True, blank=True)
    deal_text = models.CharField(max_length=255, null=True, blank=True)
    discount_percentage = models.CharField(max_length=10, null=True, blank=True)
    listing_image = models.URLField(null=True, blank=True)
    price = models.CharField(max_length=10, null=True, blank=True)
    prime_benefit_type = models.CharField(max_length=255, null=True, blank=True)
    prime_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    promotion_type = models.CharField(max_length=255, null=True, blank=True)
    parent_rating = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    parent_total_reviews = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.PROTECT)

    class Meta:
        db_table = '"amazon"."promotions"'
        verbose_name = "Promotions"
        verbose_name_plural = "Promotions"
