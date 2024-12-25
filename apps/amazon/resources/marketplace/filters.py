from django_filters.rest_framework import FilterSet

from amazon.models import Marketplace


class MarketplaceFilterSet(FilterSet):
    class Meta:
        model = Marketplace
        fields = {
            "name": ["icontains"],
            "region": ["exact"],
            "updated_on": ["date"],
        }
