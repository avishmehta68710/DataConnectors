from django_filters.rest_framework import FilterSet

from amazon.models import Inventory


class InventoryFilterSet(FilterSet):
    class Meta:
        model = Inventory
        fields = {
            "asin": ["icontains"],
            "is_qty_limit_set": ["exact"],
            "marketplace": ["exact"],
            "merchant_id": ["icontains"],
            "quantity": ["exact"],
            "title": ["icontains"],
            "url": ["icontains"],
            "updated_on": ["date"],
        }
