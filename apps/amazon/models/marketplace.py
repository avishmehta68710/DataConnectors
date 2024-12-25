from django.db import models

from core.models import BaseModel
from config import Connectors
from amazon.utils import Region


class Marketplace(BaseModel):
    """Marketplace class"""

    name = models.CharField(
        choices=Connectors.get_choices(), default=Connectors.AMAZON.value, max_length=10
    )
    region = models.CharField(
        choices=Region.get_choices(), default=Region.US.value, max_length=5
    )
    config = models.JSONField(blank=True, null=True)

    class Meta:
        db_table = '"amazon"."marketplace"'
        verbose_name = "Marketplace"
        verbose_name_plural = "Marketplaces"
