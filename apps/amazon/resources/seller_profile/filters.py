from django_filters.rest_framework import FilterSet

from amazon.models import SellerProfile


class SellerProfileFilterSet(FilterSet):
    class Meta:
        model = SellerProfile
        fields = {
            "asin": ["exact"],
            "sold_by": ["icontains"],
        }
