from django_filters.rest_framework import FilterSet

from amazon.models import Bsr


class BsrFilterSet(FilterSet):
    class Meta:
        model = Bsr
        fields = {
            "asin": ["exact"],
            "amazon_category": ["icontains"],
        }
