from django_filters.rest_framework import FilterSet

from amazon.models import Rnr


class RnrFilterSet(FilterSet):
    class Meta:
        model = Rnr
        fields = {
            "asin": ["icontains"],
            "marketplace__name": ["exact"],
        }
