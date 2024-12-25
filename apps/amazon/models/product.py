from django.db import models

from core.models import BaseModel
from amazon.models import Marketplace


class Product(BaseModel):
    """Product model"""

    asin = models.CharField(max_length=255, blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    media_alt_text = models.CharField(max_length=255, blank=True, null=True)
    deal_type = models.CharField(max_length=255, blank=True, null=True)
    deal_state = models.CharField(max_length=100, blank=True, null=True)
    deal_access_behaviour = models.CharField(max_length=100, blank=True, null=True)
    deal_early_access_duration_in_ms = models.BigIntegerField(blank=True, null=True)
    deal_percentage_claimed = models.FloatField(blank=True, null=True)
    deal_start_time = models.DateTimeField(blank=True, null=True)
    deal_end_time = models.DateTimeField(blank=True, null=True)
    deal_id = models.CharField(max_length=255, blank=True, null=True)
    mrp = models.FloatField(blank=True, null=True)
    selling_price = models.FloatField(blank=True, null=True)
    discount_percentage = models.CharField(max_length=10, blank=True, null=True)
    parent_five_star_rating_percentage = models.FloatField(blank=True, null=True)
    parent_four_star_rating_percentage = models.FloatField(blank=True, null=True)
    parent_three_star_rating_percentage = models.FloatField(blank=True, null=True)
    parent_two_star_rating_percentage = models.FloatField(blank=True, null=True)
    parent_one_star_rating_percentage = models.FloatField(blank=True, null=True)
    max_order_quantity = models.IntegerField(blank=True, null=True)
    is_max_order_quantity_set = models.BooleanField(blank=True, null=True)
    availability = models.CharField(max_length=255, blank=True, null=True)
    availability_text = models.CharField(max_length=255, blank=True, null=True)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.PROTECT)

    class Meta:
        db_table = '"amazon"."product"'
        verbose_name = "Product"
        verbose_name_plural = "Products"
