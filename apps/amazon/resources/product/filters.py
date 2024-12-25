from django_filters.rest_framework import FilterSet

from amazon.models import Product


class ProductFilterSet(FilterSet):
    class Meta:
        model = Product
        fields = {
            "asin": ["exact"],
            "marketplace__name": ["exact"],
        }
