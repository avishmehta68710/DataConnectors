from django.db import models

from core.models import BaseModel
from amazon.models import Marketplace


class Bsr(BaseModel):
    """Bsr model"""

    asin = models.CharField(max_length=255, blank=True, null=True)
    rank = models.IntegerField(null=True, blank=True)
    amazon_category = models.CharField(max_length=255, blank=True, null=True)
    offers_count = models.IntegerField(null=True, blank=True)
    rank_category = models.CharField(max_length=255, blank=True, null=True)
    thumbnail_image = models.URLField(null=True, blank=True)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.PROTECT)

    class Meta:
        db_table = '"amazon"."bsr"'
        verbose_name = "Best Seller Rank"
        verbose_name_plural = "Best Seller Ranks"
