from django_filters.rest_framework import FilterSet

from amazon.models import Promotions


class PromotionsFilterSet(FilterSet):
    class Meta:
        model = Promotions
        fields = {
            "marketplace": ["exact"],
            "asin": ["exact"],
            "promotion_type": ["exact"],
        }
